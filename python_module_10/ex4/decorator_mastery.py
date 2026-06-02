#!/usr/bin/env python3

from collections.abc import Callable
import functools
import time
from typing import Any

type CastSpellType = Callable[..., str]
type PowerValidatorType = Callable[[CastSpellType], CastSpellType]


def spell_timer(func: CastSpellType) -> CastSpellType:
    @functools.wraps(func)
    def timer(*args: Any, **kwargs: Any) -> str:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return res
    return timer


def power_validator(min_power: int) -> PowerValidatorType:
    def decorator(func: CastSpellType) -> CastSpellType:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            try:
                if "power" in kwargs:
                    power = int(kwargs["power"])
                elif args:
                    if hasattr(args[0], "__class__") and len(args) >= 3:
                        power = int(args[2])
                    else:
                        power = int(args[0])
                else:
                    power = 0
                if power >= min_power:
                    return func(*args, **kwargs)
                return "Insufficient power for this spell"
            except Exception:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[[CastSpellType], CastSpellType]:
    def decorator(func: CastSpellType) -> CastSpellType:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < (max_attempts - 1):
                        print(("Spell failed, retrying... "
                               f"(attempt {attempt + 1}/{max_attempts})"))
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    fail_count = 0

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        nonlocal fail_count
        if fail_count < 3:
            fail_count += 1
            raise RuntimeError("Fizzle")
        return "Waaaaaaagh spelled !"
    print(unstable_spell())
    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G3"))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Fireball", power=5))


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error:\n{err}")

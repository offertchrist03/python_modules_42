#!/usr/bin/env python3

from collections.abc import Callable
import functools
import time

type CastSpellType = Callable[..., str]
type PowerValidatorType = Callable[[CastSpellType], CastSpellType]


def spell_timer(func: CastSpellType) -> CastSpellType:
    @functools.wraps(func)
    def timer(*args, **kwargs) -> str:
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
        def wrapper(*args, **kwargs) -> str:
            if len(args) == 2:
                power = args[0]
            elif len(args) == 3:
                power = args[2]
            else:
                power = kwargs.get("power", 0)

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[[CastSpellType], CastSpellType]:
    def decorator(func: CastSpellType) -> CastSpellType:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(("Spell failed, retrying... "
                           f"(attempt {attempt}/{max_attempts})"))
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


if __name__ == "__main__":
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
        global fail_count
        if fail_count < 3:
            fail_count += 1
            raise RuntimeError("Fizzle")
        return "Waaaaaaagh spelled !"

    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G3"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))

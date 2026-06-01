#!/usr/bin/env python3

import time
from collections.abc import Callable
import functools

type CastSpellType = Callable[..., str]
type PowerValidatorType = Callable[[CastSpellType], CastSpellType]


def spell_timer(func: CastSpellType) -> CastSpellType:
    @functools.wraps(func)
    def timer(spell_name: str, power: int) -> str:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        res = func(spell_name, power)
        end = time.perf_counter()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return res
    return timer


def power_validator(min_power: int) -> PowerValidatorType:
    def decorator(func: CastSpellType) -> CastSpellType:
        @functools.wraps(func)
        def wrapper(power: int, target: str) -> str:
            if power >= min_power:
                return func(target, power)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> CastSpellType:
    count = 1

    def retry(func: CastSpellType) -> str:
        nonlocal count
        while count <= max_attempts:
            try:
                return func()
            except Exception:
                count += 1
                print(f"Spell failed, retrying... ({count}/{max_attempts})")
        return "Spell casting failed after max_attempts attempts"
    return retry

# class MageGuild:
#     @staticmethod
#     def validate_mage_name(name: str) -> bool
#     def cast_spell(self, spell_name: str, power: int) -> str

#!/usr/bin/env python3

import functools
from functools import reduce, partial, lru_cache
from collections.abc import Callable
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    OPERATION: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }
    try:
        op = OPERATION.get(operation)
        if op:
            return reduce(op, spells)
        else:
            raise Exception()
    except Exception:
        raise ValueError('Support operations: "add", "multiply", "max", "min"')


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, Callable[[str], str]]:
    res: dict[str, Callable[[str], str]] = {}
    res['air_enchant'] = partial(base_enchantment, 50, 'air')
    res['fire_enchant'] = partial(base_enchantment, 50, 'fire')
    res['earth_enchant'] = partial(base_enchantment, 50, 'earth')
    return res


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(damage: int) -> str:
        return f"Damage spell: {damage} damage"

    @dispatch.register(str)
    def _(enchant: str) -> str:
        return f"Enchantment: {enchant}"

    @dispatch.register(list)
    def _(spells: list[Any]) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return dispatch

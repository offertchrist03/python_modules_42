#!/usr/bin/env python3

from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def accumulator(cumul: int) -> int:
        nonlocal total
        total += cumul
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchantment


type memory_vault_callable = Callable[[str, str], None] | Callable[[str], str]


def memory_vault() -> dict[str, memory_vault_callable]:
    memory: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        if key and value:
            memory[key] = value

    def recall(key: str) -> str:
        if key in memory.keys():
            return memory[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}

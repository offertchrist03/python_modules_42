#!/usr/bin/env python3

from typing import Any
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


type memory_vault_callable = Callable[..., Any]


def memory_vault() -> dict[str, memory_vault_callable]:
    memory: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        try:
            if key and value:
                memory[key] = value
        except Exception:
            pass

    def recall(key: str) -> str:
        if key in memory.keys():
            return memory[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    for i in range(2):
        print(f"counter_a call {i + 1}: {counter_a()}")
    counter_b = mage_counter()
    for i in range(1):
        print(f"counter_b call {i + 1}: {counter_b()}")

    print()
    print("Testing spell accumulator...")
    cumul_a = spell_accumulator(100)
    base = cumul_a(0)
    print(f"Base {base}, add 20: {cumul_a(20)}")
    print(f"Base {base}, add 20: {cumul_a(30)}")

    print()
    print("Testing enchantment factory...")
    flame = enchantment_factory("Flaming")
    froze = enchantment_factory("Frozen")
    print(f"{flame('Sword')}")
    print(f"{froze('Shield')}")

    print("Testing memory vault...")
    vault = memory_vault()
    store: Callable[[str, str], None] = vault['store']
    recall: Callable[[str], str] = vault['recall']
    print("Store 'secret' = 42")
    store("secret", "42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error:\n{err}")
    except KeyboardInterrupt:
        pass

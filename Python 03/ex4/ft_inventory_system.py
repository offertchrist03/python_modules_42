#!/usr/bin/env python3

import sys


def find_index(char: str, s: str) -> int:
    i: int = 0
    for c in s:
        if c == char:
            return i
        i += 1
    return -1


def find_occ(char: str, s: str) -> int:
    i: int = 0
    occ: int = 0
    for c in s:
        if c == char:
            occ += 1
        i += 1
    return occ


def key_exists(key: str, dicts: dict[str, int]) -> int:
    for key_d in dicts.keys():
        if key == key_d:
            return 1
    return -1


def str_list(strings: list[str], sep: str) -> str:
    try:
        text: str = ""
        i: int = 0
        for string in strings:
            string = f"{string}"
            if (i < len(strings) - 1):
                text = text + string + sep
            else:
                text = text + string
            i += 1
        return text
    except Exception as err:
        raise Exception(f"Error: {err}")


def str_list_int(integers: list[int], sep: str) -> str:
    try:
        text: str = ""
        i: int = 0
        for integer in integers:
            string: str = f"{integer}"
            if (i < len(integers) - 1):
                text = text + string + sep
            else:
                text = text + string
            i += 1
        return text
    except Exception as err:
        raise Exception(f"Error: {err}")


def parse_key_value(s: str) -> tuple[str, int]:
    try:
        sep: int = find_index(':', s)
        if find_occ(':', s) != 1:
            raise ValueError(f"Error - invalid parameter {s!r}")
        key: str = s[:sep]
        try:
            value: int = int(s[sep+1:])
        except ValueError as err:
            raise ValueError(f"Quantity error for '{key}': {err}")
        return (key, value)
    except Exception as err:
        raise Exception(err)


def add_new_item(new_item: str, inventory: dict[str, int]) -> None:
    try:
        key, value = parse_key_value(new_item)
        if key_exists(key, inventory) == 1:
            raise ValueError(f"Redundant item '{key}' - discarding")
        else:
            inventory[key] = int(value)
    except (ValueError, KeyError, Exception) as err:
        print(err)


def parse_argv(argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in argv:
        add_new_item(arg, inventory)
    return inventory


def get_max_item(inventory: dict[str, int]) -> str:
    max_key: str = ""
    for item in inventory:
        if max_key == "":
            max_key = item
        else:
            if inventory[max_key] < inventory[item]:
                max_key = item
    return max_key


def get_min_item(inventory: dict[str, int]) -> str:
    min_key: str = ""
    for item in inventory:
        if min_key == "":
            min_key = item
        else:
            if inventory[min_key] > inventory[item]:
                min_key = item
    return min_key


def inventory_summary(inventory: dict[str, int]) -> None:
    total_items: int = sum(inventory.values())
    for item in inventory:
        percent: float = round((inventory[item] / total_items) * 100, 1)
        print(f"Item {item} represents {percent}%")

    max_item: str = get_max_item(inventory)
    print(
        f"Item most abundant: {max_item} with quantity {inventory[max_item]}")
    min_item: str = get_min_item(inventory)
    print(
        f"Item least abundant: {min_item} with quantity {inventory[min_item]}")


def ft_inventory_system() -> None:
    if (len(sys.argv) < 1):
        return
    argv: list[str] = sys.argv[1:]
    if (len(argv) < 1):
        return

    inventory: dict[str, int] = parse_argv(argv)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")
    print(
        (f"Total quantity of the {len(inventory.keys())} "
         f"items: {sum(inventory.values())}")
    )

    inventory_summary(inventory)

    add_new_item("magic_item:1", inventory)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_inventory_system()

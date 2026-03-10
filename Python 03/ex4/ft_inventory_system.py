#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/05 11:59:30 by mahendri            #+#    #+#            #
#   Updated: 2026/03/05 11:59:30 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_split(text: str, sep: str) -> list[str]:
    try:
        word_count: int = sum(char == sep for char in text) + 1

        parts: list[str] = [""] * word_count
        part_index: int = 0
        i: int = 0
        start: int = 0
        for char in text:
            if char == sep:
                parts[part_index] = text[start:i]
                part_index += 1
                start = i + 1
            i += 1
        if (part_index == word_count - 1):
            parts[part_index] = text[start:i]
        return parts
    except Exception as err:
        print(f"Error: {err}")
        return [""]


def str_list(strings: list, sep: str) -> str:
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
        print(f"Error: {err}")
        return ""


def handle_parse(string: str) -> dict[str, int]:
    try:
        item: dict[str, int] = {}
        if (len(ft_split(string, ':')) <= 1):
            raise Exception("Usage = <item>:<value>")
        [key, value] = ft_split(string, ':')
        item.update({key: int(value)})
    except ValueError as err:
        print(f"Error : {err}")
        return {}
    except Exception as err:
        print(f"Error : {err}")
        return {}
    else:
        return item


def parse_dict(argv: list[str]) -> dict[str, int]:
    try:
        inventory: dict[str, int] = {}
        for arg in argv:
            item = handle_parse(arg)
            inventory.update(item)
    except Exception as err:
        print(f"Error : {err}")
        raise Exception("Please verify your inputs")
    else:
        return inventory


def inventory_analysis(inventory: dict[str, int]) -> list[int]:
    total_items: int = 0
    total_items += sum(inventory.values())

    res: list[int] = [total_items, len(inventory)]
    return res


def show_current_inventory(inventory: dict[str, int]) -> None:
    [total_items, inventory_len] = inventory_analysis(inventory)
    for [key, value] in inventory.items():
        percent: float = (value / total_items) * 100
        print(f"{key}: {value} ({percent:.1f}%)")


def get_min_max(inventory: dict[str, int]) -> dict[str, int]:
    try:
        min_max: dict[str, int] = {}
        if (len(inventory) == 1):
            min_max = inventory
            return min_max

        min_value: int = min(inventory.values())
        for [key, value] in inventory.items():
            if value == min_value:
                min_max[key] = value
                break

        max_value: int = max(inventory.values())
        for [key, value] in inventory.items():
            if value == max_value:
                min_max[key] = value
                break
    except Exception as err:
        print(f"Error : {err}")
        raise Exception(err)
    else:
        return min_max


def restock_suggestion(inventory: dict[str, int]) -> dict[str, int]:
    if len(inventory) <= 1:
        return inventory

    need: dict[str, int] = {}
    min_max_items: dict[str, int] = get_min_max(inventory)
    [min_value, max_value] = min_max_items.values()

    for [key, value] in inventory.items():
        if min_value >= value:
            need.update({key: value})

    return need


def categorize_moderates_scarces(inventory: dict[str, int]) -> list[
    dict[str, int]
]:
    try:
        min_max_items: dict[str, int] = get_min_max(inventory)
        [min_item, max_item] = min_max_items.items()
        average: int = max_item[1] - min_item[1]

        moderates: dict[str, int] = {}
        for [key, value] in inventory.items():
            if (value >= average):
                moderates[key] = value

        scarces: dict[str, int] = {}
        for [key, value] in inventory.items():
            if (value < average):
                scarces[key] = value
    except Exception as err:
        print(f"Error : {err}")
        return []
    else:
        res: list[dict[str, int]] = [moderates, scarces]
        return res


def ft_inventory_system() -> None:
    if (len(sys.argv) < 1):
        return
    argv: list[str] = sys.argv[1:]
    if (len(argv) < 1):
        return

    try:
        inventory: dict[str, int] = parse_dict(argv)
    except Exception as err:
        print(f"Error : {err}")
    else:
        print("=== Inventory System Analysis ===")
        [total_items, inventory_len] = inventory_analysis(inventory)
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {inventory_len}")

        print()
        print("=== Current Inventory ===")
        show_current_inventory(inventory)

        print()
        print("=== Inventory Statistics ===")
        if len(inventory) > 1:
            min_max_items = get_min_max(inventory)
            [min_item, max_item] = min_max_items.items()
            print(f"Most abundant: {max_item[0]} ({max_item[1]} units)")
            print(f"Least abundant: {min_item[0]} ({min_item[1]} unit)")
        else:
            inventory_list_key: list[str] = [key
                                             for key in inventory.keys()]
            inventory_list_value: list[int] = [value
                                               for value in inventory.values()]
            print("Most abundant: "
                  f"{str_list(inventory_list_key, ',')} "
                  f"({str_list(inventory_list_value, '')} units)")
            print(f"Least abundant: "
                  f"{str_list(inventory_list_key, ',')} "
                  f"({str_list(inventory_list_value, '')} units)")

            print()
            print("=== Item Categories ===")
            if len(inventory) > 1:
                [moderates, scarces] = categorize_moderates_scarces(inventory)
                print(f"Moderate: {moderates}")
                print(f"Scarce: {scarces}")
            else:
                print(f"Moderate: {inventory}")
                print(f"Scarce: {inventory}")

            print()
            print("=== Management Suggestions ===")
            restock = restock_suggestion(inventory)
            print(f"Restock needed: {restock}")

            print()
            print("=== Dictionary Properties Demo ===")
            print(f"Dictionary keys: {str_list(inventory_list_key, ', ')}")
            print("Dictionary values: "
                  f"{str_list(inventory_list_value, ', ')}")
            print("Sample lookup - 'sword' in inventory: "
                  f"{not not (inventory.get('sword'))}")


if __name__ == "__main__":
    ft_inventory_system()

#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{filename}'")
        file = open(filename, "r")
        print("---")
        print()
        print(file.read())
        print()
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
    except Exception as err:
        print(f"Error opening file '{filename}': {err}")


if __name__ == "__main__":
    main()

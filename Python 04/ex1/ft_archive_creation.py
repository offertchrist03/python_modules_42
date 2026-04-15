#!/usr/bin/env python3

import sys


def show_content(text: str) -> None:
    print("---")
    print()
    print(text)
    print()
    print("---")


def open_read() -> str | None:
    if len(sys.argv) <= 1:
        print("Usage: ft_archive_creation.py <file>")
        return None

    filename: str = sys.argv[1]
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{filename}'")
        file = open(filename, "r")
        content: str = file.read()
        show_content(content)
        file.close()
        print(f"File '{filename}' closed.")
        return content
    except FileNotFoundError as err:
        print(f"Error opening file '{filename}': {err}")
    except PermissionError as err:
        print(f"Error opening file '{filename}': {err}")
    except Exception as err:
        print(f"Error opening file '{filename}': {err}")


def transform_data(data: str) -> str:
    new_data = ""
    for c in data:
        if c == '\n':
            new_data += '#'
        new_data += c
    new_data += '#'
    return new_data


def save_content(data: str) -> None:
    save_as: str = input("Enter new file name (or empty): ")
    if not save_as:
        print("Not saving data.")
        return
    file = open(save_as, 'w')
    _: int = file.write(data)
    return


if __name__ == "__main__":
    content: str | None = open_read()
    if not content:
        exit(0)

    new_content = transform_data(content)
    show_content(new_content)
    save_content(new_content)

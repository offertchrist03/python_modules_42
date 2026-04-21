#!/usr/bin/env python3

import sys


def show_content(text: str) -> None:
    print("---")
    print()
    print(text)
    print()
    print("---")


def open_read() -> str | None:
    if len(sys.argv) != 2:
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
    except Exception as err:
        print(f"Error opening file '{filename}': {err}")


def transform_data(data: str) -> str:
    new_data = ""
    try:
        for c in data:
            if c == '\n':
                new_data += '#'
            new_data += c
        new_data += '#'
    except Exception:
        pass
    return new_data


def save_content(data: str) -> None:
    try:
        save_as: str = input("Enter new file name (or empty): ")
        if not save_as:
            print("Not saving data.")
            return
        try:
            file = open(save_as, 'w')
            _: int = file.write(data)
            file.close()
        except Exception as err:
            print(f"Error opening file '{save_as}': {err}")
    except KeyboardInterrupt:
        print("Stopped.")
    return


if __name__ == "__main__":
    content: str | None = open_read()
    if not content:
        exit(0)

    new_content = transform_data(content)
    show_content(new_content)
    save_content(new_content)

#!/usr/bin/env python3

def garden_operations() -> None:
    number: float = 0
    string: str = "abc"
    dic: dict[str, str] = {"name": "koto"}

    print("Testing ValueError...")
    try:
        number = int(string)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except Exception:
        print("Error")

    print("")
    print("Testing ZeroDivisionError...")
    try:
        number = 125 / number
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except Exception:
        print("Error")

    print("")
    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except Exception:
        print("Error")

    print("")
    print("Testing KeyError...")
    try:
        string = dic["_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    except Exception:
        print("Error")

    print("")
    print("Testing multiple errors together...")
    try:
        number = int(string)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    except Exception:
        print("Error")

    print()
    print("All error types tested successfully!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("")

    garden_operations()


if __name__ == "__main__":
    test_error_types()

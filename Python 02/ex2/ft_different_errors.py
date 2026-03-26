#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        _num: float = int("abc")
        print(_num)
    if operation_number == 1:
        _num = 78 / 0
        print(_num)
    if operation_number == 2:
        _file = open('/non/existent/file')
        print(_file.read())
    if operation_number == 3:
        _str: str = "hello " + 42
        print(_str)
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        try:
            garden_operations(i)
        except ValueError as err:
            print(f"Caught ValueError: {err}")
        except ZeroDivisionError as err:
            print(f"Caught ZeroDivisionError: {err}")
        except FileNotFoundError as err:
            print(f"Caught FileNotFoundError: {err}")
        except TypeError as err:
            print(f"Caught TypeError: {err}")
        except Exception as err:
            print(f"Caught Exception: {err}")
    print("Operation completed successfully")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

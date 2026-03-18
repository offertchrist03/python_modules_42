#!/usr/bin/env python3

def check_temperature(temp_str: str | None) -> int:
    try:
        try:
            if temp_str is None:
                raise ValueError()
            temp: int = int(temp_str)
        except ValueError:
            print(f"Error: '{temp_str}' is not a valid number")
            return -1

        if (temp < 0):
            raise ValueError(
                (f"Error: {temp_str}°C"
                 " is too cold for plants (min 0°C)")
            )
        elif (temp > 40):
            raise ValueError(
                (f"Error: {temp_str}°C"
                 " is too hot for plants (max 40°C)")
            )
        print(f"Temperature {temp_str}°C is perfect for plants!")
        return temp
    except ValueError as err:
        print(err)
        return -1
    except Exception as err:
        print(f"Exception Error:\n{err}")
        return -1


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_cases: list[str | None] = ["25", "abc", "100", "-50", None]

    for case in test_cases:
        print(f"Testing temperature: {case}")
        _: int = check_temperature(case)
        print("")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()

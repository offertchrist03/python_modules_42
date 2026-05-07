#!/usr/bin/env python3

def input_temperature(temp_str: str | None) -> int:
    print(f"Input data is '{temp_str}'")
    if temp_str is None:
        raise ValueError("Error temp_str is None")
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    print(f"Temperature is now 25°C '{temp}'")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_cases: list[str | None] = ["25", "abc", "100", "-50", None]

    for case in test_cases:
        try:
            _: int = input_temperature(case)
        except ValueError as err:
            print(f"Caught input_temperature error: {err}")
        except Exception as err:
            print(f"Exception Error:\n{err}")
        print("")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

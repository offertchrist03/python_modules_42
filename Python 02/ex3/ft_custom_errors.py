#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, err: str) -> None:
        if not err:
            err = "Unknown garden error"
        error: str = "Caught GardenError: " + err
        Exception.__init__(self, error)


class PlantError(Exception):
    def __init__(self, err: str) -> None:
        if not err:
            err = "Unknown plant error"
        error: str = "Caught PlantError: " + err
        Exception.__init__(self, error)


class WaterError(Exception):
    def __init__(self, err: str) -> None:
        if not err:
            err = "Unknown water error"
        error: str = "Caught WaterError: " + err
        Exception.__init__(self, error)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as err:
        print(err)
    except Exception:
        print("Error")

    print("")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as err:
        print(err)
    except Exception:
        print("Error")

    print("")
    print("Testing catching all garden errors...")
    try:
        try:
            raise GardenError("The tomato plant is wilting!")
        except GardenError as err:
            print(err)
        except Exception:
            print("Error")

        try:
            raise GardenError("Not enough water in the tank!")
        except GardenError as err:
            print(err)
    except Exception:
        print("Error")

    print("")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()

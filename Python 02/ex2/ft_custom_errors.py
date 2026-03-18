#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, err: str) -> None:
        Exception.__init__(self, "Caught a garden error: " + err)


class PlantError(GardenError):
    def __init__(self, err: str) -> None:
        Exception.__init__(self, "Caught PlantError: " + err)


class WaterError(GardenError):
    def __init__(self, err: str) -> None:
        Exception.__init__(self, "Caught WaterError: " + err)


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

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


def water_plant(plant_name: str | None) -> None:
    if plant_name is None or not plant_name:
        raise PlantError("Invalid plant name")

    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    valid_plants: list[str] = ["Tomato", "Lettuce", "Carrots"]

    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as err:
        print(err)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print()
    non_valid_plants: list[str] = ["Tomato", "lettuce", "Carrots"]

    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plant in non_valid_plants:
            water_plant(plant)
    except PlantError as err:
        print(err)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

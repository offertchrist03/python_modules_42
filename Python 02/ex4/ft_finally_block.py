#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, err: str = "Unknown garden error") -> None:
        Exception.__init__(self, err)


class PlantError(GardenError):
    def __init__(self, err: str = "Unknown plant error") -> None:
        error: str = "Caught PlantError: " + err
        GardenError.__init__(self, error)


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
    except GardenError as err:
        print(err)
        print(".. ending tests and returning to main")
    except Exception:
        print("Error")
    finally:
        print("Closing watering system")

    print()
    non_valid_plants: list[str] = ["Tomato", "lettuce", "Carrots"]

    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        for plant in non_valid_plants:
            water_plant(plant)
    except GardenError as err:
        print(err)
        print(".. ending tests and returning to main")
    except Exception:
        print("Error")
    finally:
        print("Closing watering system")

    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

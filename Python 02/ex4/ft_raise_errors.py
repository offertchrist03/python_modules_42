#!/usr/bin/env python3

class CheckPlantHealthError(Exception):
    def __init__(self, err: str) -> None:
        Exception.__init__(self, "Error: " + err)


def check_plant_health(
    plant_name: str | None,
    water_level: int,
    sunlight_hours: int
) -> str | None:
    res: bool = True
    try:
        if plant_name is None:
            raise CheckPlantHealthError("Plant name cannot be empty!")
        elif water_level < 1:
            raise CheckPlantHealthError(
                f"Water level {water_level} is too low (min 1)"
            )
        elif water_level > 10:
            raise CheckPlantHealthError(
                f"Water level {water_level} is too high (max 10)"
            )
        elif sunlight_hours < 2:
            raise CheckPlantHealthError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        elif sunlight_hours > 12:
            raise CheckPlantHealthError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
    except CheckPlantHealthError as err:
        res = False
        print(err)
    except Exception:
        print("Error")

    if res:
        return (f"Plant '{plant_name}' is healthy!")
    return None


def test_plant_checks() -> None:
    string: str | None = None

    print("=== Garden Plant Health Checker ===")

    print("")
    print("Testing good values...")
    string = check_plant_health("tomato", 5, 7)
    if string is not None:
        print(string)

    print("")
    print("Testing empty plant name...")
    string = check_plant_health(None, 5, 7)
    if string is not None:
        print(string)

    print("")
    print("Testing bad water level...")
    string = check_plant_health("tomato", 15, 7)
    if string is not None:
        print(string)

    print("")
    print("Testing bad sunlight hours...")
    string = check_plant_health("tomato", 5, 0)
    if string is not None:
        print(string)

    print("")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

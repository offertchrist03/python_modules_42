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


class CheckPlantHealthError(GardenError):
    def __init__(self, err: str) -> None:
        Exception.__init__(self, "Error " + err)


class GardenManager:
    def __init__(self, water_tank: int) -> None:
        self.plants: list[dict | None] = [None] * 1024
        self.plant_count: int = 0
        self.water_tank: int = water_tank

    def add_plant(
        self,
        plant_name: str | None,
        water_level: int,
        sunlight_hours: int
    ) -> None:
        try:
            if plant_name is None:
                raise CheckPlantHealthError(
                    "adding plant: Plant name cannot be empty!"
                )
            plant: dict = {
                "plant_name": plant_name,
                "water_level": water_level,
                "sunlight_hours": sunlight_hours
            }
            self.plants[self.plant_count] = plant
            self.plant_count += 1
            print(f"Added {plant_name} successfully")
        except CheckPlantHealthError as err:
            print(err)
        except Exception:
            print("Error")

    def garden_recovery(self) -> None:
        encountered_err: bool = False
        try:
            if self.water_tank < self.plant_count:
                raise GardenError("Not enough water in tank")
        except GardenError as err:
            print(err)
            encountered_err = True
        except Exception:
            print("Error")

        if encountered_err:
            print("System recovered and continuing...")
            self.water_tank = self.plant_count

    def check_plants(self) -> None:
        try:
            try:
                plant_list: list[dict | None] = self.plants
                index: int = 0
                for plant in plant_list:
                    if plant is not None:
                        self.check_plant_health(
                            plant['plant_name'],
                            plant['water_level'],
                            plant['sunlight_hours']
                        )
                        index += 1
                        if index == self.plant_count:
                            break
            except Exception:
                raise PlantError("on checking plants")
        except PlantError as err:
            print(err)
        except Exception:
            print("Error")

    def water_plants(self) -> None:
        curr_plant: str = ""
        plant_list: list[dict | None] = self.plants
        index: int = 0
        print("Opening watering system")
        try:
            try:
                for plant in plant_list:
                    if plant is None:
                        print("Error: Cannot water None"
                              " - invalid plant!")
                        break
                    else:
                        curr_plant = plant['plant_name']
                        print(f"Watering {curr_plant} - success")
                        index += 1
                        self.water_tank -= 1
                        if index == self.plant_count:
                            break
            except Exception:
                raise WaterError("Cannot water {curr_plant}"
                                 " - invalid plant!")
        except WaterError as err:
            print(err)
        except Exception:
            print("Error")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
    ) -> None:
        res: bool = True
        try:
            if plant_name is None:
                raise CheckPlantHealthError("Plant name cannot be empty!")
            elif water_level < 1:
                raise CheckPlantHealthError(
                    f"checking {plant_name}: Water level {water_level} "
                    "is too low (min 1)"
                )
            elif water_level > 10:
                raise CheckPlantHealthError(
                    f"checking {plant_name}: Water level {water_level} "
                    "is too high (max 10)"
                )
            elif sunlight_hours < 2:
                raise CheckPlantHealthError(
                    f"checking {plant_name}: Sunlight hours {sunlight_hours} "
                    "is too low (min 2)"
                )
            elif sunlight_hours > 12:
                raise CheckPlantHealthError(
                    f"checking {plant_name}: Sunlight hours {sunlight_hours} "
                    "is too high (max 12)"
                )
        except CheckPlantHealthError as err:
            res = False
            print(err)
        except Exception:
            print("Error")
        if res:
            print(f"{plant_name}: healthy "
                  f"(water: {water_level}, sun: {sunlight_hours})")


if __name__ == "__main__":
    print("=== Garden Management System ===")

    garden: GardenManager = GardenManager(3)

    print("")
    print("Adding plants to garden...")
    garden.add_plant("tomato", 5, 8)
    garden.add_plant("lettuce", 15, 8)
    garden.add_plant(None, 15, 8)

    print("")
    print("Watering plants...")
    garden.water_plants()

    print("")
    print("Checking plant health...")
    garden.check_plants()

    print("")
    print("Testing error recovery...")
    garden.garden_recovery()

    print("")
    print("Garden management system test complete!")

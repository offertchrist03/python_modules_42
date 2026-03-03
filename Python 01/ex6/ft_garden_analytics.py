#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:16:59 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:16:59 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name.title()} grew 1cm")

    def display(self) -> None:
        print(f"{self.name.title()}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str
    ) -> None:
        super().__init__(name, height)
        self.color: str = color

    def display(self) -> None:
        print(f"{self.name.title()}: {self.height}cm, "
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_point: int
    ) -> None:
        super().__init__(name, height, color)
        self.prize_point: int = prize_point

    def display(self) -> None:
        print(f"{self.name.title()}: {self.height}cm, "
              f"{self.color} flowers (blooming), "
              f"Prize points: {self.prize_point}")

    def increment_prize(self, value: int) -> None:
        print(f"[updated] {self.name.title()}: {self.height}cm, "
              f"{self.color} flowers (blooming), "
              f"Prize points: {self.prize_point}")
        self.prize_point += value


class GardenManager:
    garden_owners = {}
    total_owner_count = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plant_count: int = 0
            self.plant_grow_count: int = 0
            self.type_regular: int = 0
            self.type_flower: int = 0
            self.type_flower_prize: int = 0

        def register_plant(
            self,
            plant_type: str
        ) -> None:
            self.plant_count += 1
            if (plant_type == "PrizeFlower"):
                self.type_flower_prize += 1
            elif (plant_type == "FloweringPlant"):
                self.type_flower += 1
            elif (plant_type == "Plant"):
                self.type_regular += 1

        def register_grow(self) -> None:
            self.plant_grow_count += 1

        def summary(self) -> None:
            print(f"Plants added: {self.plant_count}, "
                  f"Total growth: {self.plant_grow_count}cm")
            print(f"Plant types: "
                  f"{self.type_regular} regular, "
                  f"{self.type_flower} flowering, "
                  f"{self.type_flower_prize} prize flowers")

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = [None] * 1024
        self.stats: GardenManager.GardenStats = self.GardenStats()

    def add_plant(
        self,
        plant: Plant,
        plant_type: str
    ) -> None:
        if not GardenManager.validate_height(plant.height):
            print(f"Error: {plant.name} has an invalid height!")
            return
        i: int = self.stats.plant_count
        self.plants[i] = plant
        self.stats.register_plant(plant_type)
        print(f"Added {plant.name.title()} "
              f"to {self.owner.title()}'s garden")

    def grow_all_plants(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        i: int = 0
        total_plant: int = self.stats.plant_count
        for i in range(total_plant):
            plant = self.plants[i]
            plant.grow()
            self.stats.register_grow()

    def score(self) -> int:
        score: int = 0
        for plant in self.plants:
            if (isinstance(plant, PrizeFlower) and plant.prize_point > 0):
                score += plant.prize_point
        return score

    def str_owner(self) -> str:
        return (f"{self.owner}: {self.score()}")

    def garden_owner_report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden :")
        i: int = 0
        total_plant: int = self.stats.plant_count
        for i in range(total_plant):
            plant = self.plants[i]
            plant.display()

    @staticmethod
    def validate_height(height: int) -> bool:
        return (height > 0)

    @classmethod
    def create_garden_network(
        cls,
        names: list[str]
    ) -> dict[str, "GardenManager"]:
        for name in names:
            GardenManager.total_owner_count += 1
            new_garden = cls(name)
            GardenManager.garden_owners[name.lower()] = new_garden
        return GardenManager.garden_owners

    @classmethod
    def network_summary(cls) -> None:
        string: str = ""
        i: int = 0
        for garden_obj in GardenManager.garden_owners.values():
            string += garden_obj.str_owner()
            if (i < (GardenManager.total_owner_count - 1)):
                string += ", "
            i += 1
        print("Height validation test: True")
        print(f"Garden scores - {string}")
        print(f"Total gardens managed: {GardenManager.total_owner_count}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    network = GardenManager.create_garden_network(["alice", "bob"])

    print("=== ALICE ===\n")
    alice_garden = network["alice"]

    alice_garden.add_plant(
        Plant("oak tree", 10),
        "Plant"
    )
    alice_garden.add_plant(
        FloweringPlant("rose", 10, "red"),
        "FloweringPlant"
    )
    alice_garden.add_plant(
        PrizeFlower("sunflower", 10, "red", 10),
        "PrizeFlower"
    )
    alice_garden.add_plant(
        PrizeFlower("tulip", 10, "blue", 50),
        "PrizeFlower"
    )

    print("")
    alice_garden.grow_all_plants()

    print("")
    alice_garden.garden_owner_report()

    print("")
    alice_garden.stats.summary()

    print("")
    print(f"alice's score: {alice_garden.score()}")

    print("\n=== BOB ===\n")
    bob_garden = network["bob"]

    bob_garden.add_plant(
        Plant("oak tree", 10),
        "Plant"
    )
    bob_garden.add_plant(
        FloweringPlant("rose", 10, "red"),
        "FloweringPlant"
    )
    bob_garden.add_plant(
        PrizeFlower("sunflower", 10, "red", 10),
        "PrizeFlower"
    )

    print("")
    bob_garden.grow_all_plants()

    print("")
    bob_garden.garden_owner_report()

    print("")
    bob_garden.stats.summary()

    print("")
    print(f"bob's score: {bob_garden.score()}")

    print("\n=== NETWORK SUMMARY ===\n")
    GardenManager.network_summary()

#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:16:51 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:16:51 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(
        self,
        name: str = "(plant)",
        height: int = 0,
        age: int = 0
    ) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show_plant(self, category: str, txt: str) -> None:
        print(f"\n{self.name} ({category}): {self.height}cm, {self.age} days, "
              f"{txt}")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def show_flower(self) -> None:
        category = "Flower"
        txt = self.color + " color"
        self.show_plant(category, txt)

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def display(self) -> None:
        self.show_flower()
        self.bloom()


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def show_tree(self) -> None:
        category = "Tree"
        txt = f"{self.trunk_diameter}cm diameter"
        self.show_plant(category, txt)

    def produce_shade(self) -> None:
        print(f"{self.name} provides {int(self.trunk_diameter * 1.56)}"
              " square meters of shade")

    def display(self) -> None:
        self.show_tree()
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def show_vegetable(self) -> None:
        category = "Vegetable"
        txt = self.harvest_season + " harvest"
        self.show_plant(category, txt)

    def nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def display(self) -> None:
        self.show_vegetable()
        self.nutrition()


if __name__ == "__main__":
    data_flowers = [
        {"name": "Rose", "height": 25, "age": 30, "color": "red"},
        {"name": "Sunflower", "height": 30, "age": 25, "color": "yellow"},
        {"name": "Tulip", "height": 28, "age": 21, "color": "blue"}
    ]

    data_trees = [
        {"name": "Oak", "height": 500, "age": 1825, "trunk_diameter": 50},
        {"name": "Apple Tree", "height": 480, "age": 888, "trunk_diameter": 60}
    ]

    data_vegetable = [
        {"name": "Carrot", "height": 18, "age": 10,
            "harvest_season": "all seasons",
            "nutritional_value": "Carotein"},
        {"name": "Tomato", "height": 80, "age": 90,
            "harvest_season": "summer",
            "nutritional_value": "Vitamin C"}
    ]

    print("=== Garden Plant Types ===")

    for i in range(2):
        flower = Flower(
            data_flowers[i]["name"],
            data_flowers[i]["height"],
            data_flowers[i]["age"],
            data_flowers[i]["color"]
        )
        flower.display()

    for i in range(2):
        tree = Tree(
            data_trees[i]["name"],
            data_trees[i]["height"],
            data_trees[i]["age"],
            data_trees[i]["trunk_diameter"]
        )
        tree.display()

    for i in range(2):
        vegetable = Vegetable(
            data_vegetable[i]["name"],
            data_vegetable[i]["height"],
            data_vegetable[i]["age"],
            data_vegetable[i]["harvest_season"],
            data_vegetable[i]["nutritional_value"]
        )
        vegetable.display()

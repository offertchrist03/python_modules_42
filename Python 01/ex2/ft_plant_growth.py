#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:16:25 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:16:25 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: int, init_age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.init_age: int = init_age

    def get_info(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.init_age} days old"
        )

    def grow(self, value: int) -> None:
        self.height += value

    def age(self, value: int) -> None:
        self.init_age += value


def week_growth(plant: Plant) -> None:
    print("=== Day 1 ===")
    plant.get_info()

    for i in range(6):
        plant.grow(1)
        plant.age(1)

    print("=== Day 7 ===")
    plant.get_info()

    print(f"Growth this week: +{i + 1}cm")


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    week_growth(plant)

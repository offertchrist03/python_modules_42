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

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.init_age} days"
        )

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.init_age += 1


def week_growth(plant: Plant) -> None:
    print("=== Day 1 ===")
    plant.show()
    i = 0
    for i in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.show()
    print(f"Growth this week: +{i + 1}cm")


if __name__ == "__main__":
    p = Plant("Rose", 25, 30)
    week_growth(p)

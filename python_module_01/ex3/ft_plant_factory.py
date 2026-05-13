#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:16:35 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:16:35 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(
        self,
        name: str = "(plant)",
        height: int = 0,
        init_age: int = 0
    ) -> None:
        self.name: str = name
        self.height: int = height
        self.init_age: int = init_age

    def show(self) -> None:
        print(
            f"Created: {self.name} ({self.height}cm, {self.init_age} days)"
        )


if __name__ == "__main__":
    data_plants = [
        {"name": "Rose", "height": 25, "init_age": 30},
        {"name": "Oak", "height": 200, "init_age": 365},
        {"name": "Cactus", "height": 5, "init_age": 90},
        {"name": "Sunflower", "height": 80, "init_age": 45},
        {"name": "Fern", "height": 15, "init_age": 120}
    ]

    plants: list[Plant] = [None] * 5
    i: int = 0
    print("=== Plant Factory Output ===")
    for i in range(5):
        plants[i] = Plant(
            data_plants[i]["name"],
            data_plants[i]["height"],
            data_plants[i]["init_age"]
        )
        plants[i].show()
    print(f"\nTotal plants created: {i + 1}")

#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:16:18 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:16:18 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.age} days"
        )


if __name__ == "__main__":
    plants = [
        Plant("Rose", 15, 20),
        Plant("Hibiscus", 80, 130),
        Plant("Tomato", 30, 30),
        Plant("Sunflower", 150, 60)
    ]

    print("=== Garden Plant Registry ===")
    i = 0
    for i in range(4):
        plants[i].show()

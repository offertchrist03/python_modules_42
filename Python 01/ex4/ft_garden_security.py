#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:16:42 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:16:42 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(
        self, name: str = "(plant)",
        height: int = 0,
        age: int = 0
    ) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show_created(self):
        print(f"Plant created: {self.name}")

    def show_current(self):
        print(f"Current plant: {self.name} "
              f"({self.height}cm, {self.age} days)")


class SecurePlant:
    def __init__(
        self,
        plant: Plant
    ) -> Plant:
        self.__plant: Plant = plant

    def set_height(self, new_value) -> None:
        if (new_value < 0):
            print("\nInvalid operation attempted: "
                  f"height {new_value}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return
        self.__plant.height = new_value
        print(f"Height updated: {self.__plant.height}cm [OK]")

    def set_age(self, new_value) -> None:
        if (new_value < 0):
            print("\nInvalid operation attempted: "
                  f"{new_value} days [REJECTED]")
            print("Security: Negative age rejected\n")
            return
        self.__plant.age = new_value
        print(f"Age updated: {self.__plant.age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose")
    rose.show_created()
    secure_rose = SecurePlant(rose)
    secure_rose.set_height(25)
    secure_rose.set_age(30)
    secure_rose.set_height(-5)
    rose.show_current()

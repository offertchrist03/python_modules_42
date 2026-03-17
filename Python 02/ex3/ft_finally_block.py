#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 11:31:33 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 11:31:33 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class InvalidPlantName(Exception):
    def __init__(self, err: str) -> None:
        Exception.__init__(self, err)
        self.err: str = err


def water_plants(plant_list: list[str | None]) -> None:
    res: bool = True
    index: int = 0
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                break
            else:
                char: str = plant[0]
                rest: str = plant[1:]
                print(f"Watering {char + rest}...")
                index += 1
    except (TypeError, IndexError):
        print(f"Error: Cannot water {plant_list[index]} - invalid plant!")
        res = False
    except Exception:
        print("Error")
    finally:
        print("Closing watering system (cleanup)")
    if res:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("")
    plants: list[str | None] = ["rose", "tulip", "sunflower"]
    water_plants(plants)

    print("")
    plants = ["oak tree", None]
    water_plants(plants)

    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

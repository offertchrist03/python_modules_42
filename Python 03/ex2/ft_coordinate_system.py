#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/03 13:40:03 by mahendri            #+#    #+#            #
#   Updated: 2026/03/03 13:40:03 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import math


def parsing_coordinates(arg: str) -> tuple[int, int, int]:
    splited: list[str] = arg.split(',')
    if len(splited) < 1:
        return (0, 0, 0)
    try:
        numbers: list[int] = [0, 0, 0]
        i: int = 0
        for s in splited:
            n = int(s)
            numbers[i] = n
            i += 1
            if (i == 3):
                break
    except ValueError:
        raise ValueError(
            "Error parsing coordinates: "
            f"invalid literal for int() with base 10: '{s}'"
        )
        return None
    else:
        return (numbers[0], numbers[1], numbers[2])


def distance_between_coord(
            initial: tuple[int, int, int],
            current: tuple[int, int, int]
        ) -> float:
    distance: float = 0
    (x1, y1, z1) = initial
    (x2, y2, z2) = current
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def unpack_coord(coord: tuple[int, int, int]) -> None:
    (x, y, z) = coord
    print(f"Player at x={x}, y={y}, z={z}")


def ft_coordinate_system() -> None:
    argv: list[str] = sys.argv[1:]
    argv_len: int = len(argv)
    if (argv_len < 1 or argv_len > 3):
        print("No coordinations provided. "
              "Usage: python3 ft_coordinate_system.py <x>,<y>,<z> ...")
        return
    try:
        coord = parsing_coordinates(argv[0])
    except ValueError as err:
        print(err)
        print("Error details - Type: ValueError, "
              f"Args: (\"{err}\",)")
    except Exception as err:
        print(f"Unexpected error: {err}")
    else:
        print(f"Parsed position: {coord}")
        unpack_coord(coord)
        distance: float = distance_between_coord((0, 0, 0), coord)
        print(f"Distance between (0, 0, 0) and {coord}: {distance:.2f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    ft_coordinate_system()

#!/usr/bin/env python3

import math


def ft_len(s: str | list[str] | list[int] | None) -> int:
    i: int = 0

    if s is None:
        return i
    for _ in s:
        i += 1
    return i


def splice_tuple(s: str) -> tuple[float, float, float]:
    try:
        num_list: list[str] = s.split(',')
        float_list: list[float] = []
        for num in num_list:
            float_list += [float(num)]

        if ft_len(num_list) != 3:
            raise Exception("Invalid syntax")

        for n in num_list:
            try:
                float_list += [float(n)]
            except ValueError as err:
                raise ValueError(f"Error on parameter {n}: '{err}'")

        res: tuple[float, float, float] = (
            float(float_list[0]), float(float_list[1]), float(float_list[2]))
        return res
    except Exception as err:
        raise Exception(err)


def get_player_pos() -> tuple[float, float, float]:
    while True:
        ask: str = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        try:
            coord: tuple[float, float, float] = splice_tuple(ask)
            return coord
        except Exception as err:
            print(err)


def calcul_distance(
    coord1: tuple[float, float, float],
    coord2: tuple[float, float, float]
) -> float:
    (x1, y1, z1) = coord1
    (x2, y2, z2) = coord2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return round(distance, 4)


def game_coordinates() -> None:
    try:
        (x1, y1, z1) = get_player_pos()
        print(f"Got a first tuple: {(x1, y1, z1)}")
        print(f"It includes: X={x1} Y={y1} Z={z1}")
        center_distance: float = calcul_distance((0, 0, 0), (x1, y1, z1))
        print(
            f"Distance to center: {center_distance}")

        print()
        print("Get a second set of coordinates")
        (x2, y2, z2) = get_player_pos()
        two_distance: float = calcul_distance((x1, y1, z1), (x2, y2, z2))
        print(f"Distance between the 2 sets of coordinates: {two_distance}")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    try:
        game_coordinates()
    except KeyboardInterrupt:
        print("Stopped")
    except Exception as err:
        print(f"Error: {err}")

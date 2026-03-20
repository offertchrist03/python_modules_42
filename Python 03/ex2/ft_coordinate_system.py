#!/usr/bin/env python3

import math


def ft_len(s: str | list[str] | list[int] | None) -> int:
    i: int = 0

    if s is None:
        return i
    for _ in s:
        i += 1
    return i


def splice_num(i: int, sep: str, s: str) -> str:
    res: str = ""
    s_len: int = ft_len(s)

    while i < s_len:
        if s[i] == " ":
            i += 1
        if not s[i] == sep:
            res += s[i]
        if s[i] == sep:
            i += 1
            break
        i += 1
    return res


def splice_tuple(s: str) -> tuple[float, float, float]:
    try:
        i: int = 0
        s_len: int = ft_len(s)
        num_list: list[str] = []
        float_list: list[float] = []
        while i < s_len:
            num: str = splice_num(i, ',', s)
            if ft_len(num) > 0:
                num_list += [num]
                i += ft_len(num) + 1
            else:
                i += 1

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


def ask_tuple() -> tuple[float, float, float]:
    while True:
        ask: str = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        coord: tuple[float, float, float] = splice_tuple(ask)
        return coord


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
        (x1, y1, z1) = ask_tuple()
        print(f"Got a first tuple: {(x1, y1, z1)}")
        print(f"It includes: X={x1} Y={y1} Z={z1}")
        center_distance: float = calcul_distance((0, 0, 0), (x1, y1, z1))
        print(
            f"Distance to center: {center_distance}")

        print()
        print("Get a second set of coordinates")
        (x2, y2, z2) = ask_tuple()
        two_distance: float = calcul_distance((x1, y1, z1), (x2, y2, z2))
        print(f"Distance between the 2 sets of coordinates: {two_distance}")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    game_coordinates()

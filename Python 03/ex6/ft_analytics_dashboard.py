#!/usr/bin/env python3

import random


def gen_score(players: list[str], mean: int = 0) -> dict[str, int]:
    scored_players: dict[str, int] = {}
    score: int = 0
    for p in players:
        score = random.randint(0 + mean, 1000 + mean)
        scored_players[p] = score
    return scored_players


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()

    initial_players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin',
        'Liam']

    print(f"Initial list of players: {initial_players}")

    capitalised_players: list[str] = [p.capitalize() for p in initial_players]
    print(f"New list with all names capitalized: {capitalised_players}")

    players: list[str] = [p
                          for p in initial_players
                          if p == p.capitalize()]
    print(f"New list of capitalized names only: {players}")

    scored_players: dict[str, int] = gen_score(players)
    print(f"Score dict: {scored_players}")

    score_mean: float = sum(scored_players.values()) / len(scored_players)
    print(f"Score average is {round(score_mean, 2)}")

    scored_players = gen_score(players, int(score_mean))
    print(f"High scores: {scored_players}")

#!/usr/bin/env python3

import random


class Common:
    def __init__(self) -> None:
        self._all_achievements: set[str] = set({
            'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
            'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
            'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
            'Boss Slayer'})


class Player(Common):
    def __init__(self, name: str) -> None:
        Common.__init__(self)
        self.name: str = name
        self.achievements: set[str] = set()

        self.random_achievements()

    def random_achievements(self) -> None:
        all_achievements: set[str] = self._all_achievements
        list_achievements: list[str] = [
            achievement
            for achievement in all_achievements]

        for _ in range(len(list_achievements)):
            try:
                i: int = random.randint(0, len(list_achievements))
                achievement: str = list_achievements[i]
                self.achievements.add(achievement)
            except Exception:
                pass

    def display(self) -> None:
        print(f"Player {self.name}: {self.achievements}")


def get_distinct_achievements(players: list[Player]) -> set[str]:
    distincts: set[str] = set()
    for player in players:
        for achievement in player.achievements:
            distincts.add(achievement)
    return distincts


def get_common_achievements(players: list[Player]) -> set[str]:
    commons: set[str] = set(players[0].achievements)
    for player in players[1:]:
        achievements: set[str] = player.achievements
        commons = commons.intersection(achievements)
    return commons


def get_unique_achievements(user: Player, players: list[Player]) -> set[str]:
    uniques: set[str] = set(user.achievements)
    for player in players:
        if player.name != user.name:
            uniques = uniques.difference(player.achievements)
    return uniques


def print_uniques(players: list[Player]) -> None:
    for player in players:
        uniques: set[str] = get_unique_achievements(
            player, players)
        print(f"Only {player.name} has: {uniques}")


def get_missing_achievements(user: Player, players: list[Player]) -> set[str]:
    others: set[str] = set()
    for player in players:
        if player.name != user.name:
            others |= player.achievements
    return others - user.achievements


def print_missings(players: list[Player]) -> None:
    for player in players:
        missings: set[str] = get_missing_achievements(player, players)
        print(f"{player.name} is missing: {missings}")


def gen_player_achievements() -> None:
    alice = Player("Alice")
    alice.display()

    bob = Player("Bob")
    bob.display()

    charlie = Player("Charlie")
    charlie.display()

    dylan = Player("Dylan")
    dylan.display()

    print()
    distincts: set[str] = get_distinct_achievements(
        [alice, bob, charlie, dylan])
    print(f"All distinct achievements: {distincts}")

    print()
    commons: set[str] = get_common_achievements(
        [alice, bob, charlie, dylan])
    print(f"Common achievements: {commons}")

    print()
    print_uniques([alice, bob, charlie, dylan])

    print()
    print_missings([alice, bob, charlie, dylan])


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    gen_player_achievements()

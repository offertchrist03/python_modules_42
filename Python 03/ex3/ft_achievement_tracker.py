#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/03 16:56:52 by mahendri            #+#    #+#            #
#   Updated: 2026/03/03 16:56:52 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def get_unique_achievements() -> set[str]:
    unique_achievements: set[str] = set()
    datas: list[str] = ['boss_slayer', 'collector', 'first_kill', 'level_10',
                        'perfectionist', 'speed_demon', 'treasure_hunter']
    for data in datas:
        unique_achievements.add(data)
    return unique_achievements


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.achievements: set[str] = set()

    def add_achievements(self, achievements: list[str]) -> None:
        for achievement in achievements:
            if achievement is None:
                print("Achievement invalid.")
                return
            self.achievements.add(achievement)

    def show_achievements(self) -> None:
        print(f"Player {self.name} achievements: {self.achievements}")

    def get_achievements(self) -> set[str]:
        return self.achievements


def get_common_achievements(players: list[Player]) -> set[str]:
    players_count: int = len(players)

    if players_count < 1:
        return set()
    elif players_count == 1:
        return players[0].get_achievements()

    i: int = 0
    common_achievements: set[str] = set()
    common_achievements.update(players[i].get_achievements())

    i += 1
    while i < players_count:
        next_player = players[i].get_achievements()
        common_achievements = common_achievements & next_player
        i += 1

    return common_achievements


def get_diff_achievements(players: list[Player]) -> set[str]:
    players_count: int = len(players)

    if players_count < 1:
        return set()
    elif players_count == 1:
        return players[0].get_achievements()

    i: int = 0
    diff: set[str] = set()
    diff.update(players[i].get_achievements())

    i += 1
    while i < players_count:
        diff_2: set[str] = set()
        next_player = players[i].get_achievements()
        diff_1 = diff - next_player
        diff_2 = next_player - diff
        diff = diff_1 | diff_2
        i += 1

    common = get_common_achievements(players)
    diff = diff - common

    return diff


def vs_diff_achievements(player_1: Player, player_2: Player) -> set[str]:
    try:
        if player_1 is None or player_2 is None:
            return set()

        diff: set[str] = set()
        diff = player_1.get_achievements() - player_2.get_achievements()
    except Exception as err:
        print(f"Error: {err}")
        return set()
    else:
        return diff


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    alice = Player("alice")
    alice.add_achievements(['first_kill', 'level_10',
                            'treasure_hunter', 'speed_demon'])
    alice.show_achievements()

    bob = Player("bob")
    bob.add_achievements(['first_kill', 'level_10',
                          'boss_slayer', 'collector'])
    bob.show_achievements()

    charlie = Player("charlie")
    charlie.add_achievements(['level_10', 'treasure_hunter',
                              'boss_slayer', 'speed_demon', 'perfectionist'])
    charlie.show_achievements()

    print()
    print("=== Achievement Analytics ===")
    all_unique_achievements: set[str] = get_unique_achievements()
    print(f"All unique achievements: {all_unique_achievements}")
    print(f"Total unique achievements: {len(all_unique_achievements)}")

    print()
    common_achievements: set[str] = get_common_achievements(
                                        [alice, bob, charlie]
                                    )
    diff_achievements: set[str] = get_diff_achievements(
                                        [alice, bob, charlie]
                                    )
    print(f"Common to all players: {common_achievements}")
    print(f"Rare achievements (1 player): {diff_achievements}")

    print()
    print(f"Alice vs Bob common: {get_common_achievements([alice, bob])}")
    print(f"Alice unique: {vs_diff_achievements(alice, bob)}")
    print(f"Bob unique: {vs_diff_achievements(bob, alice)}")

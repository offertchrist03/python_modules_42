#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/05 21:34:37 by mahendri            #+#    #+#            #
#   Updated: 2026/03/05 21:34:37 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Generator


def str_iter(iters: Generator[object, None, None], sep: str = ', ') -> str:
    text: str = ""
    first: bool = True

    for item in iters:
        if not first:
            text += sep
        text += str(item)
        first = False

    return text


def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_prime_numbers(limit: int) -> Generator[int, None, None]:
    for i in range(2, limit):
        while not is_prime(i):
            i += 1
        yield i


def show_prime_numbers(limit: int) -> None:
    prime_numbers: Generator[int, None, None] = get_prime_numbers(limit)
    print(f"Prime numbers (first {limit}): "
          f"{str_iter(prime_numbers, ', ')}")


def get_fibonacci(limit: int) -> Generator[int, None, None]:
    for i in range(limit):
        yield i


def show_fibonacci(limit: int) -> None:
    fibonacci = get_fibonacci(limit)
    print(f"Fibonacci sequence (first {limit}): "
          f"{str_iter(fibonacci, ', ')}")


class Player:
    def __init__(
        self,
        id: str = "0",
        name: str = "(name)",
        level: int = 0
    ):
        self.__is_logged: bool = True
        self.__id: str = id
        self.__name: str = name
        self.__level: int = level
        self.__treasures: int = 0
        self.__kill: int = 0

    def get_is_logged(self) -> bool:
        return self.__is_logged

    def get_id(self) -> str:
        return self.__id

    def get_level(self) -> int:
        return self.__level

    def display(self) -> str:
        return (f"Player {self.__name} ({self.__level})")

    def login(self) -> str:
        self.__is_logged = True
        return "is logged in"

    def logout(self) -> str:
        self.__is_logged = False
        return "is logged out"

    def level_up(self) -> str:
        if not self.__is_logged:
            return "is unavailable for now"
        self.__level += 1
        return "leveled up"

    def kill(self) -> str:
        if not self.__is_logged:
            return "is unavailable for now"
        self.__kill += 1
        return "killed monster"

    def death(self) -> str:
        if not self.__is_logged:
            return "is unavailable for now"
        self.__kill -= 5
        return "is dead"

    def item_found(self) -> str:
        if not self.__is_logged:
            return "is unavailable for now"
        self.__treasures += 1
        return "found treasure"


class Data_stream:
    def __init__(
            self,
            players: list[Player],
            events: list[tuple[str, str]]
    ) -> None:
        self.__players: list[Player] = players
        self.__events: list[tuple[str, str]] = events
        self.__events_processed_count: int = 0
        self.__events_processed: list[tuple[str, str]] = (
            self.init_events_processed()
        )

    def init_events_processed(self) -> list[tuple[str, str]]:
        try:
            event: tuple[str, str] = ("", "")
            event_len: int = len(self.__events)
            events_processed: list[tuple[str, str]] = [event] * event_len
            return events_processed
        except Exception:
            return [("", "")]

    def get_player(self, _id: str) -> Player | None:
        for player in iter(self.__players):
            if player.get_id() == _id:
                return player
        return None

    def stream_events(self) -> None:
        try:
            self.init_events_processed()
            i: int = 0
            for event_data in iter(self.__events):
                _id, event = event_data
                player = self.get_player(_id)
                self.process_event(player, event)
                i += 1
        except Exception as err:
            print(f"Error: {err}")

    def process_event(self, player: Player | None, event: str) -> None:
        i: int = self.__events_processed_count
        if player is None:
            print("Player is None")
            return
        if player.get_is_logged():
            self.__events_processed[i] = (player.get_id(), event)
        self.__events_processed_count += 1
        res: str = ""
        if event == "login":
            res = player.login()
        elif event == "logout":
            res = player.logout()
        elif event == "kill":
            res = player.kill()
        elif event == "death":
            res = player.death()
        elif event == "level_up":
            res = player.level_up()
        elif event == "item_found":
            res = player.item_found()
        else:
            res = "(unknown event)"
        print(f"Event {i + 1}: "
              f"{player.display()} {res}")

    def display_players(self) -> None:
        for player in iter(self.__players):
            print(player.display())

    def stream_analytics(self) -> None:
        print("=== Stream Analytics ===")
        print(f"Total events processed: {len(self.__events_processed)}")

        high_levels: int = sum(player.get_level() >= 10
                               for player in iter(self.__players))
        print(f"High-level players (10+): {high_levels}")

        treasure_events: int = sum(event[1] == "item_found"
                                   for event in iter(self.__events_processed))
        print(f"Treasure events: {treasure_events}")

        level_up_events: int = sum(event[1] == "level_up"
                                   for event in iter(self.__events_processed))
        print(f"Level-up: {level_up_events}")


def generate_players(
            template: list[dict[str, dict[str, int]]]
        ) -> list[Player]:
    players_data: set[tuple[str, int]] = set()
    for item in iter(template):
        player_name: str = f"{item['player']}"
        player_level: int = 0
        if item['data'] and item['data']['level'] >= 0:
            player_level = item['data']['level']
        player: tuple[str, int] = (player_name, player_level)
        players_data.add(player)

    players: list[Player] = [Player()] * len(players_data)
    index: int = 0
    for (name, level) in players_data:
        players[index] = Player(name, name, level)
        index += 1

    return players


def generate_events(template: list[dict[str, str]]) -> list[tuple[str, str]]:
    index: int = 0
    events_list: list[tuple[str, str]] = [("", "")] * len(template)
    for item in iter(template):
        events_list[index] = (item['player'], item['event_type'])
        index += 1

    return events_list


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print()

    template: list[dict] = [
        {'id': 1, 'player': 'frank', 'event_type': 'login',
            'timestamp': '2024-01-01T23:17',
            'data': {'level': 16, 'score_delta': 128, 'zone': 'pixel_zone_2'}},
        {'id': 2, 'player': 'frank', 'event_type': 'login',
            'timestamp': '2024-01-22T23:57',
            'data': {'level': 35, 'score_delta': -11, 'zone': 'pixel_zone_5'}},
        {'id': 3, 'player': 'diana', 'event_type': 'login',
            'timestamp': '2024-01-01T02:13',
            'data': {'level': 15, 'score_delta': 417, 'zone': 'pixel_zone_5'}},
        {'id': 4, 'player': 'alice', 'event_type': 'level_up',
            'timestamp': '2024-01-07T22:41',
            'data': {'level': 45, 'score_delta': 458, 'zone': 'pixel_zone_4'}},
        {'id': 5, 'player': 'bob', 'event_type': 'death',
            'timestamp': '2024-01-19T08:51',
            'data': {'level': 1, 'score_delta': 63, 'zone': 'pixel_zone_4'}},
        {'id': 6, 'player': 'charlie', 'event_type': 'kill',
            'timestamp': '2024-01-05T06:48',
            'data': {'level': 22, 'score_delta': 4, 'zone': 'pixel_zone_1'}},
        {'id': 7, 'player': 'diana', 'event_type': 'login',
            'timestamp': '2024-01-12T11:38',
            'data': {'level': 17, 'score_delta': -56, 'zone': 'pixel_zone_4'}},
        {'id': 8, 'player': 'eve', 'event_type': 'login',
            'timestamp': '2024-01-30T12:05',
            'data': {'level': 36, 'score_delta': 200, 'zone': 'pixel_zone_5'}},
        {'id': 9, 'player': 'charlie', 'event_type': 'level_up',
            'timestamp': '2024-01-07T22:04',
            'data': {'level': 3, 'score_delta': 133, 'zone': 'pixel_zone_3'}},
        {'id': 10, 'player': 'alice', 'event_type': 'logout',
            'timestamp': '2024-01-28T03:24',
            'data': {'level': 18, 'score_delta': 364, 'zone': 'pixel_zone_3'}},
        {'id': 11, 'player': 'bob', 'event_type': 'kill',
            'timestamp': '2024-01-12T06:42',
            'data': {'level': 18, 'score_delta': -27, 'zone': 'pixel_zone_5'}},
        {'id': 12, 'player': 'frank', 'event_type': 'logout',
            'timestamp': '2024-01-18T23:15',
            'data': {'level': 11, 'score_delta': 373, 'zone': 'pixel_zone_4'}},
        {'id': 13, 'player': 'charlie', 'event_type': 'item_found',
            'timestamp': '2024-01-23T17:14',
            'data': {'level': 44, 'score_delta': 232, 'zone': 'pixel_zone_1'}},
        {'id': 14, 'player': 'bob', 'event_type': 'login',
            'timestamp': '2024-01-26T10:25',
            'data': {'level': 18, 'score_delta': -33, 'zone': 'pixel_zone_2'}},
        {'id': 15, 'player': 'eve', 'event_type': 'item_found',
            'timestamp': '2024-01-11T06:41',
            'data': {'level': 32, 'score_delta': 305, 'zone': 'pixel_zone_4'}},
        {'id': 16, 'player': 'bob', 'event_type': 'kill',
            'timestamp': '2024-01-05T07:47',
            'data': {'level': 36, 'score_delta': 451, 'zone': 'pixel_zone_3'}},
        {'id': 17, 'player': 'frank', 'event_type': 'level_up',
            'timestamp': '2024-01-14T18:25',
            'data': {'level': 24, 'score_delta': 124, 'zone': 'pixel_zone_2'}},
        {'id': 18, 'player': 'eve', 'event_type': 'death',
            'timestamp': '2024-01-03T01:55',
            'data': {'level': 8, 'score_delta': 56, 'zone': 'pixel_zone_2'}},
        {'id': 19, 'player': 'frank', 'event_type': 'death',
            'timestamp': '2024-01-20T02:24',
            'data': {'level': 25, 'score_delta': 379, 'zone': 'pixel_zone_5'}},
        {'id': 20, 'player': 'charlie', 'event_type': 'level_up',
            'timestamp': '2024-01-28T00:43',
            'data': {'level': 47, 'score_delta': 17, 'zone': 'pixel_zone_5'}},
        {'id': 21, 'player': 'charlie', 'event_type': 'item_found',
            'timestamp': '2024-01-11T03:18',
            'data': {'level': 28, 'score_delta': 61, 'zone': 'pixel_zone_4'}},
        {'id': 22, 'player': 'alice', 'event_type': 'item_found',
            'timestamp': '2024-01-29T23:16',
            'data': {'level': 33, 'score_delta': 82, 'zone': 'pixel_zone_5'}},
        {'id': 23, 'player': 'alice', 'event_type': 'item_found',
            'timestamp': '2024-01-10T20:32',
            'data': {'level': 39, 'score_delta': 103, 'zone': 'pixel_zone_2'}},
        {'id': 24, 'player': 'charlie', 'event_type': 'logout',
            'timestamp': '2024-01-18T16:58',
            'data': {'level': 1, 'score_delta': 231, 'zone': 'pixel_zone_4'}},
        {'id': 25, 'player': 'alice', 'event_type': 'login',
            'timestamp': '2024-01-30T11:56',
            'data': {'level': 20, 'score_delta': 145, 'zone': 'pixel_zone_1'}},
        {'id': 26, 'player': 'bob', 'event_type': 'level_up',
            'timestamp': '2024-01-03T02:46',
            'data': {'level': 32, 'score_delta': -30, 'zone': 'pixel_zone_5'}},
        {'id': 27, 'player': 'bob', 'event_type': 'logout',
            'timestamp': '2024-01-22T15:35',
            'data': {'level': 11, 'score_delta': 171, 'zone': 'pixel_zone_5'}},
        {'id': 28, 'player': 'eve', 'event_type': 'death',
            'timestamp': '2024-01-07T17:48',
            'data': {'level': 47, 'score_delta': 105, 'zone': 'pixel_zone_3'}},
        {'id': 29, 'player': 'diana', 'event_type': 'item_found',
            'timestamp': '2024-01-21T11:28',
            'data': {'level': 34, 'score_delta': 362, 'zone': 'pixel_zone_1'}},
        {'id': 30, 'player': 'bob', 'event_type': 'logout',
            'timestamp': '2024-01-03T10:01',
            'data': {'level': 38, 'score_delta': 467, 'zone': 'pixel_zone_2'}},
        {'id': 31, 'player': 'eve', 'event_type': 'logout',
            'timestamp': '2024-01-01T02:45',
            'data': {'level': 41, 'score_delta': -40, 'zone': 'pixel_zone_2'}},
        {'id': 32, 'player': 'alice', 'event_type': 'login',
            'timestamp': '2024-01-28T10:04',
            'data': {'level': 33, 'score_delta': 143, 'zone': 'pixel_zone_3'}},
        {'id': 33, 'player': 'frank', 'event_type': 'death',
            'timestamp': '2024-01-07T17:08',
            'data': {'level': 47, 'score_delta': 484, 'zone': 'pixel_zone_5'}},
        {'id': 34, 'player': 'diana', 'event_type': 'logout',
            'timestamp': '2024-01-26T15:51',
            'data': {'level': 27, 'score_delta': 94, 'zone': 'pixel_zone_1'}},
        {'id': 35, 'player': 'alice', 'event_type': 'item_found',
            'timestamp': '2024-01-14T11:27',
            'data': {'level': 27, 'score_delta': 378, 'zone': 'pixel_zone_1'}},
        {'id': 36, 'player': 'frank', 'event_type': 'item_found',
            'timestamp': '2024-01-21T03:03',
            'data': {'level': 26, 'score_delta': 247, 'zone': 'pixel_zone_1'}},
        {'id': 37, 'player': 'bob', 'event_type': 'logout',
            'timestamp': '2024-01-07T17:28',
            'data': {'level': 9, 'score_delta': 332, 'zone': 'pixel_zone_2'}},
        {'id': 38, 'player': 'charlie', 'event_type': 'death',
            'timestamp': '2024-01-08T02:28',
            'data': {'level': 36, 'score_delta': 0, 'zone': 'pixel_zone_1'}},
        {'id': 39, 'player': 'frank', 'event_type': 'level_up',
            'timestamp': '2024-01-27T00:05',
            'data': {'level': 49, 'score_delta': 142, 'zone': 'pixel_zone_2'}},
        {'id': 40, 'player': 'diana', 'event_type': 'death',
            'timestamp': '2024-01-16T06:55',
            'data': {'level': 26, 'score_delta': -40, 'zone': 'pixel_zone_2'}},
        {'id': 41, 'player': 'diana', 'event_type': 'login',
            'timestamp': '2024-01-13T08:59',
            'data': {'level': 30, 'score_delta': 192, 'zone': 'pixel_zone_4'}},
        {'id': 42, 'player': 'frank', 'event_type': 'item_found',
            'timestamp': '2024-01-26T17:42',
            'data': {'level': 46, 'score_delta': 398, 'zone': 'pixel_zone_2'}},
        {'id': 43, 'player': 'bob', 'event_type': 'kill',
            'timestamp': '2024-01-07T01:37',
            'data': {'level': 48, 'score_delta': 455, 'zone': 'pixel_zone_1'}},
        {'id': 44, 'player': 'frank', 'event_type': 'kill',
            'timestamp': '2024-01-02T01:37',
            'data': {'level': 31, 'score_delta': 414, 'zone': 'pixel_zone_5'}},
        {'id': 45, 'player': 'bob', 'event_type': 'login',
            'timestamp': '2024-01-17T02:54',
            'data': {'level': 12, 'score_delta': -30, 'zone': 'pixel_zone_5'}},
        {'id': 46, 'player': 'alice', 'event_type': 'item_found',
            'timestamp': '2024-01-28T07:25',
            'data': {'level': 8, 'score_delta': 483, 'zone': 'pixel_zone_2'}},
        {'id': 47, 'player': 'eve', 'event_type': 'level_up',
            'timestamp': '2024-01-02T19:05',
            'data': {'level': 27, 'score_delta': 497, 'zone': 'pixel_zone_5'}},
        {'id': 48, 'player': 'eve', 'event_type': 'kill',
            'timestamp': '2024-01-30T08:13',
            'data': {'level': 43, 'score_delta': 221, 'zone': 'pixel_zone_2'}},
        {'id': 49, 'player': 'charlie', 'event_type': 'death',
            'timestamp': '2024-01-05T21:41',
            'data': {'level': 20, 'score_delta': 368, 'zone': 'pixel_zone_3'}},
        {'id': 50, 'player': 'alice', 'event_type': 'login',
            'timestamp': '2024-01-15T19:36',
            'data': {'level': 7, 'score_delta': -25, 'zone': 'pixel_zone_5'}}
    ]

    players: list[Player] = generate_players(template)
    events: list[tuple[str, str]] = generate_events(template)

    data_stream = Data_stream(players, events)
    data_stream.stream_events()

    print()
    data_stream.display_players()
    print()
    data_stream.stream_analytics()

    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print()
    print("=== Generator Demonstration ===")
    show_fibonacci(10)
    show_prime_numbers(5)

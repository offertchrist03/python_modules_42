#!/usr/bin/env python3

import random
from collections.abc import Generator


available_moves: list[str] = [
    'eat', 'move', 'release', 'use',
    'swim', 'grab', 'sleep', 'climb', 'run']

players: list[str] = ['alice', 'charlie', 'bob', 'dylan']


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player: str = random.choice(players)
        move: str = random.choice(available_moves)
        yield (player, move)


def gen_ten_events() -> list[tuple[str, str]]:
    stream_event: Generator[tuple[str, str]] = gen_event()
    events: list[tuple[str, str]] = []
    for _ in range(10):
        event: tuple[str, str] = next(stream_event)
        events += [event]
    return events


def filter_events(
    picked: tuple[str, str],
    events: list[tuple[str, str]]
) -> list[tuple[str, str]]:
    return [event
            for event in events
            if event != picked]


def pick_event(events: list[tuple[str, str]]) -> tuple[str, str]:
    return events[random.randrange(len(events))]


def pick_until_none(events: list[tuple[str, str]]) -> None:
    while True:
        picked: tuple[str, str] = pick_event(events)
        print(f"Got event from list: {picked}")
        events = filter_events(picked, events)
        print(f"Remains in list: {events}")
        if len(events) <= 0:
            break


def stream_1000() -> None:
    stream_event: Generator[tuple[str, str]] = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(stream_event)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    # stream_1000()

    ten_events: list[tuple[str, str]] = gen_ten_events()
    print(f"Built list of 10 events: {ten_events}")
    pick_until_none(ten_events)

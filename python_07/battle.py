#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def display_factory(creature: CreatureFactory) -> None:
    print("Testing factory")
    base = creature.create_base()
    print(base.describe())
    print(base.attack())
    evolved = creature.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(creature_1: CreatureFactory, creature_2: CreatureFactory) -> None:
    base_1 = creature_1.create_base()
    base_2 = creature_2.create_base()
    print(base_1.describe())
    print(" vs.")
    print(base_2.describe())
    print(" fight!")
    print(base_1.attack())
    print(base_2.attack())


if __name__ == "__main__":
    fire = FlameFactory()
    display_factory(fire)
    print()

    water = AquaFactory()
    display_factory(water)
    print()

    battle(fire, water)

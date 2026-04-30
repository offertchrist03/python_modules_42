#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def display_healing_factory(
        creature: HealingCreatureFactory
) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = creature.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    evolved = creature.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def display_transform_factory(
        creature: TransformCreatureFactory
) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base = creature.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    evolved = creature.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healer = HealingCreatureFactory()
    display_healing_factory(healer)

    print()

    transform = TransformCreatureFactory()
    display_transform_factory(transform)

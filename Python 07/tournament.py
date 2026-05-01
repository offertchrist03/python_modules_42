#!/usr/bin/env python3

from ex2 import (BattleStrategy, NormalStrategy, AggressiveStrategy,
                 DefensiveStrategy)
from ex1 import (CreatureFactory, TransformCreatureFactory,
                 HealingCreatureFactory)
from ex0 import (FlameFactory, AquaFactory)


tournament_creature_type = tuple[CreatureFactory, BattleStrategy]
battle_versus_type = list[tuple[tournament_creature_type,
                                tournament_creature_type]]


def get_class_name(classe: CreatureFactory | BattleStrategy) -> str:
    if isinstance(classe, CreatureFactory):
        if isinstance(classe, HealingCreatureFactory):
            return "Healing"
        elif isinstance(classe, TransformCreatureFactory):
            return "Transform"
        return classe.create_base().__class__.__name__
    else:
        if isinstance(classe, NormalStrategy):
            return "Normal"
        elif isinstance(classe, AggressiveStrategy):
            return "Aggressive"
        elif isinstance(classe, DefensiveStrategy):
            return "Defensive"
        else:
            return "Unknown"


def battle_names(creatures: list[tournament_creature_type]) -> str:
    creature_names: list[str] = []
    for creature, strategy in creatures:
        name: str = f"{get_class_name(creature)}+{get_class_name(strategy)}"
        creature_names += [(f"{name}")]
    res: str = f"{[f"({name})" for name in creature_names]}"
    res = res.replace("'", '')
    res = res.replace("[", '[ ')
    res = res.replace("]", ' ]')

    res += f"\n*** Tournament ***\n{len(creatures)} opponent"
    res += f"{'s' if len(creatures) > 0 else ''} involved"

    return res


def battle_versus(creatures: list[tournament_creature_type]
                  ) -> battle_versus_type:
    battles: list[tuple[tournament_creature_type,
                        tournament_creature_type]] = []

    i: int = 0
    while i < len(creatures):
        creature = creatures[i]
        for opponent in creatures[i:]:
            if get_class_name(creature[0]) != get_class_name(opponent[0]):
                battles.append((creature, opponent))
        i += 1

    return (battles)


def single(
    creatures: list[tournament_creature_type],
) -> None:
    print(f"{battle_names(creatures)}")

    battles = battle_versus(creatures)
    for creature_1, creature_2 in battles:
        print("\n* Battle *")
        print(f"{creature_1[0].create_base().describe()}")
        print(" vs.")
        print(f"{creature_2[0].create_base().describe()}")

        print(" now fight!")
        try:
            creature_1[1].act(creature_1[0].create_base())
            creature_2[1].act(creature_2[0].create_base())
        except Exception as err:
            print(f"Battle error, aborting tournament: {err}")


if __name__ == "__main__":
    fire = FlameFactory()
    water = AquaFactory()
    healer = HealingCreatureFactory()
    morph = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    agressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    tournament_0: list[tournament_creature_type] = [
        (fire, normal_strategy),
        (healer, defensive_strategy),
    ]
    single(tournament_0)

    print("Tournament 1 (error)")
    tournament_1: list[tournament_creature_type] = [
        (fire, agressive_strategy),
        (healer, defensive_strategy),
    ]
    single(tournament_1)

    print("Tournament 2 (multiple)")
    tournament_2: list[tournament_creature_type] = [
        (water, normal_strategy),
        (healer, defensive_strategy),
        (morph, agressive_strategy),
    ]
    single(tournament_2)

#!/usr/bin/env python3

from collections.abc import Callable


type SpellType = Callable[[str, int], str]


def spell_combiner(
    spell1: SpellType,
    spell2: SpellType
) -> Callable[[str, int], tuple[str, str]]:
    def combine(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combine


def power_amplifier(base_spell: SpellType, multiplier: int) -> SpellType:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: SpellType) -> SpellType:
    def caster_require(target: str, power: int) -> str:
        is_true = condition(target, power)
        if not is_true:
            return "Spell fizzled"
        return spell(target, power)
    return caster_require


def spell_sequence(
    spells: list[SpellType]
) -> Callable[[str, int], list[str]]:
    def sequences(target: str, power: int) -> list[str]:
        res: list[str] = []
        for spell in spells:
            res.append(spell(target, power))
        return res
    return sequences


def main() -> None:
    def fireball(target: str, power: int) -> str:
        if power <= 0:
            return f"Fireball hits {target}"
        return f"{power}"

    def heal(target: str, health: int) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    fireball_heal = spell_combiner(fireball, heal)
    print(("Combined spell result: "
           f"{fireball_heal('Dragon', 0)[0]}, "
           f"{fireball_heal('Dragon', 0)[1]}"))

    print()
    original_fireball = power_amplifier(fireball, 1)
    mega_fireball = power_amplifier(fireball, 3)
    print("Testing power amplifier...")
    print((f"Original: {original_fireball('Dragon', 10)}, "
           f"Amplified: {mega_fireball('Dragon', 10)}"))

    print()
    print("Testing spell sequence...")
    sequences = spell_sequence([fireball, fireball])
    for hit in sequences('Dragon', 0):
        print(hit)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error:\n{err}")
    except KeyboardInterrupt:
        pass

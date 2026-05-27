#!/usr/bin/env python3

type dicti = dict[str, str | int]
type dictd = dict[str, int | float]


def artifact_sorter(artifacts: list[dicti]) -> list[dicti]:
    res: list[dicti] = list(
        sorted(artifacts, key=lambda artifact: int(artifact['power']) * -1))
    return res


def power_filter(mages: list[dicti], min_power: int) -> list[dicti]:
    res: list[dicti] = list(
        filter(lambda mage: int(mage['power']) >= min_power, mages))
    return res


def spell_transformer(spells: list[str]) -> list[str]:
    res: list[str] = list(
        map(lambda spell: f"* {spell} *", spells)
    )
    return res


def mage_stats(mages: list[dicti]) -> dictd:
    max_power: int = max(list(
        map(lambda mage: int(mage['power']), mages)
    ))
    min_power: int = min(list(
        map(lambda mage: int(mage['power']), mages)
    ))
    average = round((sum(list(
        map(lambda mage: int(mage['power']), mages)
    )) / len(mages)), 2)
    return {"max_power": max_power,
            "min_power": min_power, "avg_power": average}

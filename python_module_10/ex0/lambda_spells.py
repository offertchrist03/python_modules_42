#!/usr/bin/env python3

type DictA = dict[str, str | int]
type DictB = dict[str, int | float]


def artifact_sorter(artifacts: list[DictA]) -> list[DictA]:
    res: list[DictA] = list(
        sorted(artifacts, key=lambda artifact: int(artifact['power']) * -1))
    return res


def power_filter(mages: list[DictA], min_power: int) -> list[DictA]:
    res: list[DictA] = list(
        filter(lambda mage: int(mage['power']) >= min_power, mages))
    return res


def spell_transformer(spells: list[str]) -> list[str]:
    res: list[str] = list(
        map(lambda spell: f"* {spell} *", spells)
    )
    return res


def mage_stats(mages: list[DictA]) -> DictB:
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

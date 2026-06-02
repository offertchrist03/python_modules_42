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


def main() -> None:
    artifacts: list[DictA] = [{'name': 'Excalibur', 'power': 64},
                              {'name': 'Oak Staff', 'power': 74},
                              {'name': 'Crystal Orb', 'power': 85},
                              {'name': 'Fire Staff', 'power': 92}]

    print("Testing artifact sorter...")
    sorteds = artifact_sorter(artifacts)
    print(
        (f"{sorteds[0]['name']} ({sorteds[0]['power']} power) comes before "
         f"{sorteds[1]['name']} ({sorteds[1]['power']} power)"))

    print()
    print("Testing power filter...")
    filtered = power_filter(artifacts, 90)
    print(filtered)

    print()
    print("Testing spell transformer...")
    spells = ['fireball', 'feal', 'shield']
    transformed = spell_transformer(spells)
    print(f"{str(transformed)[1:-1].replace('\'', '').replace(',', '')}")

    print()
    print("Testing mage stats...")
    mages: list[DictA] = [
        {'name': 'Gandalf', 'power': 150},
        {'name': 'Merlin', 'power': 160},
        {'name': 'Arthur', 'power': 85}
    ]
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error:\n{err}")
    except KeyboardInterrupt:
        pass

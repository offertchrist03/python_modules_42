from elements import create_fire, create_water
from alchemy.elements import create_earth, create_air


def healing_potion() -> str:
    res = "Healing potion brewed with "
    res += f"’[{create_earth()}]’ and ’[{create_air()}]’"
    return res


def strength_potion() -> str:
    res = "Strength potion brewed with "
    res += f"’[{create_fire()}]’ and ’[{create_water()}]’"
    return res

from ..elements import create_air
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    res = "Recipe transmuting Lead to Gold: brew "
    res += f"’[{create_air()}]’ and ’[{strength_potion()}]’"
    res += " mixed with "
    res += f"’[{create_fire()}]’"
    return res

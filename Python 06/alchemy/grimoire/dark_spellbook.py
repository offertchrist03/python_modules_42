from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    check: str = validate_ingredients(ingredients)
    action = "UNKNOWN"
    if check == "VALID":
        action = "recorded"
    elif check == "INVALID":
        action = "rejected"
    res: str = f"Spell {action}: {spell_name} ({ingredients} - {check})"
    return res

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:

    check: str = validate_ingredients(ingredients)
    action = "UNKNOWN"
    if check.endswith("INVALID"):
        action = "rejected"
    elif check.endswith("VALID"):
        action = "recorded"
    res: str = f"Spell {action}: {spell_name} ({check})"
    return res

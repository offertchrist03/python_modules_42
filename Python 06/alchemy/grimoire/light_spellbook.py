def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    check: str = validate_ingredients(ingredients)
    action = "UNKNOWN"
    if check == "VALID":
        action = "recorded"
    elif check == "INVALID":
        action = "rejected"
    res: str = f"Spell {action}: {spell_name} ({ingredients} - {check})"
    return res

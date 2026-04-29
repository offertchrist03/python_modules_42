from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    try:
        check = False
        alloweds: list[str] = dark_spell_allowed_ingredients()
        for ingredient in alloweds:
            if ingredient in ingredients:
                check = True
                break
        if not check:
            raise Exception()
        return f"{ingredients} - VALID"
    except Exception:
        return f"{ingredients} - INVALID"

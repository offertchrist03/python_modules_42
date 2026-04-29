def validate_ingredients(ingredients: str) -> str:
    try:
        from .light_spellbook import light_spell_allowed_ingredients

        check = False
        alloweds: list[str] = light_spell_allowed_ingredients()
        for ingredient in alloweds:
            if ingredient in ingredients:
                check = True
                break
        if not check:
            raise Exception()
        return f"{ingredients} - VALID"
    except Exception:
        return f"{ingredients} - INVALID"

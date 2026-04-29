from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    try:
        temp: str = ingredients
        temp = temp.replace(',', '')
        temp = temp.replace('and', '')
        temp = temp.replace('or', '')
        temp = temp.lower()

        alloweds: list[str] = dark_spell_allowed_ingredients()
        for ingredient in temp.split(" "):
            if ingredient != '' and not ingredient.strip() in alloweds:
                raise Exception()
        return f"{ingredients} - VALID"
    except Exception:
        return f"{ingredients} - INVALID"

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    try:
        ingredients = ingredients.replace(',', '')
        ingredients = ingredients.replace('and', '')
        ingredients = ingredients.replace('or', '')
        ingredients = ingredients.lower()

        alloweds: list[str] = dark_spell_allowed_ingredients()
        for ingredient in ingredients.split(" "):
            if ingredient != '' and not ingredient.strip() in alloweds:
                raise Exception()
        return "VALID"
    except Exception:
        return "INVALID"

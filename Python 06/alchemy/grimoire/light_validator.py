def validate_ingredients(ingredients: str) -> str:
    try:
        ingredients = ingredients.replace(',', '')
        ingredients = ingredients.replace('and', '')
        ingredients = ingredients.replace('or', '')
        ingredients = ingredients.lower()

        alloweds: list[str] = ["earth", "air", "fire", "water"]
        for ingredient in ingredients.split(" "):
            if ingredient != '' and not ingredient.strip() in alloweds:
                raise Exception()
        return "VALID"
    except Exception:
        return "INVALID"

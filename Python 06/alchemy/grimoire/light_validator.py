def validate_ingredients(ingredients: str) -> str:
    try:
        temp: str = ingredients
        temp = temp.replace(',', '')
        temp = temp.replace('and', '')
        temp = temp.replace('or', '')
        temp = temp.lower()

        alloweds: list[str] = ["earth", "air", "fire", "water"]
        for ingredient in temp.split(" "):
            if ingredient != '' and not ingredient.strip() in alloweds:
                raise Exception()
        return f"{ingredients} - VALID"
    except Exception:
        return f"{ingredients} - INVALID"

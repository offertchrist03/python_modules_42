from ex1.capability import HealCapability, TransformCapability
from ex0.creature_0 import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.type: str = "Grass"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str | None = None) -> str:
        res_target = ""
        if target:
            res_target = f"and {target} "
        return f"{self.name} heals itself {res_target}for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.type: str = "Grass/Fairy"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str | None = "others") -> str:
        res_target = ""
        if target:
            res_target = f"and {target} "
        return f"{self.name} heals itself {res_target}for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.type: str = "Normal"
        self.is_transformed: bool = False

    def attack(self) -> str:
        res: str = "attacks normally."
        if self.is_transformed:
            res = "performs a boosted strike!"
        return f"{self.name} {res}"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.type: str = "Normal/Dragon"
        self.is_transformed: bool = False

    def attack(self) -> str:
        res: str = "attacks normally."
        if self.is_transformed:
            res = "n unleashes a devastating morph strike!"
        return f"{self.name} {res}"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."

from ex1.capability import TransformCapability, HealCapability
from ex0.creature_0 import Creature
from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception((f"Invalid Creature '{creature.name}' "
                             "for this normal strategy"))
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception((f"Invalid Creature '{creature.name}' "
                             "for this agressive strategy"))
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception((f"Invalid Creature '{creature.name}' "
                             "for this defensive strategy"))
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

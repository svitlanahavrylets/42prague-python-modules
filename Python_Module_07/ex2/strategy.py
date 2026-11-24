from abc import ABC, abstractmethod
from ex2.capabilities import HealCapability, TransformCapability
from ex2.creature import Creature


class InvalidStrategyError(Exception):
    """Exception raised when a strategy is invalid for a creature."""
    pass


class BattleStrategy(ABC):
    """Abstract base class for battle strategies."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Check if creature is suitable for this strategy."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Perform battle actions using strategy."""
        pass


class NormalStrategy(BattleStrategy):
    """Standard attack strategy for any creature."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Aggressive strategy for transforming creatures."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    """Defensive strategy for healing creatures."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())

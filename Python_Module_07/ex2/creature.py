from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for all creatures."""

    def __init__(self, name: str, type_: str) -> None:
        self.name: str = name
        self.type_: str = type_

    def describe(self) -> str:
        """Return standard creature description."""
        return f"{self.name} is a {self.type_} type Creature"

    @abstractmethod
    def attack(self) -> str:
        """Abstract attack method."""
        pass

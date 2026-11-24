from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract basic class for all creatures"""
    def __init__(self, name: str, type_: str) -> None:
        self.name = name
        self.type_ = type_

    def describe(self) -> str:
        return f"{self.name} is a {self.type_} type Creature"

    @abstractmethod
    def attack(self) -> str:
        pass

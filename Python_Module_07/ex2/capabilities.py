from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract capability for healing."""
    @abstractmethod
    def heal(self) -> str:
        """Return heal description."""
        pass


class TransformCapability(ABC):
    """Abstract capability for transformation."""

    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

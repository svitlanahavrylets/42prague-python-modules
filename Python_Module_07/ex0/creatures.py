from ex0.creature import Creature


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", type_="Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", type_="Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", type_="Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon (Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", type_="Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"

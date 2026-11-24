class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age
        self.initial_height = height

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.age_days += 1

    def get_height(self) -> int:
        return self.height - self.initial_height

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


def ft_plant_growth() -> None:
    Rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(Rose.get_info())

    for _ in range(6):
        Rose.grow()
        Rose.age()

    print("=== Day 7 ===")
    print(Rose.get_info())
    print(f"Growth this week: +{Rose.get_height()}cm")


if __name__ == "__main__":
    ft_plant_growth()

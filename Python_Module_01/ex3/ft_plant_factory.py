class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def display_info(self) -> None:
        print(f'Created: {self.name}: ({self.height}cm, {self.age_days} days)')


def ft_plant_factory() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")

    for i in range(5):
        plants[i].display_info()

    print()
    print(f"Total plants created: {i + 1}")


if __name__ == "__main__":
    ft_plant_factory()

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_base_info(self) -> str:
        class_name = self.__class__.__name__
        return (f"{self.name.capitalize()} ({class_name}): "
                f"{self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(
            self, name: str, height: int, age: int, color: str
            ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def display_status(self) -> None:
        print(f"{self.get_base_info()}, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self, name: str, height: int, age: int, trunk_diameter: int
                 ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def display_status(self) -> None:
        print(f"{self.get_base_info()}, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        radius = self.trunk_diameter / 10
        shade_area = 3.14 * (radius ** 2)
        print(f"{self.name.capitalize()} provides "
              f"{int(shade_area)} square meters of shade")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: int, age: int,  harvest_season: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def display_status(self) -> None:
        print(f"{self.get_base_info()}, {self.harvest_season} harvest")

    def nutritional_value(self) -> None:
        if self.harvest_season == "summer":
            print(f"{self.name.capitalize()} is rich in vitamin C")
        else:
            print(f"{self.name.capitalize()} isn't rich in vitamin C")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("rose", 25, 30, "red"),
        Flower("tulip", 15, 10, "yellow")
        ]
    trees = [
        Tree("oak", 500, 1825, 50),
        Tree("pine", 300, 1000, 30)
        ]
    vegies = [
        Vegetable("tomato", 80, 90, "summer"),
        Vegetable("carrot", 20, 60, "winter")
        ]

    for i in range(2):
        print()
        flowers[i].display_status()
        flowers[i].bloom()

        print()
        trees[i].display_status()
        trees[i].produce_shade()

        print()
        vegies[i].display_status()
        vegies[i].nutritional_value()


if __name__ == "__main__":
    ft_plant_types()

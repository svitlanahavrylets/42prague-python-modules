class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.plant_type = "regular"

    def get_base_info(self) -> str:
        class_name = self.__class__.__name__
        return (f"{self.name.capitalize()} ({class_name}): "
                f"{self.height}cm, {self.age} days")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.plant_type = "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(
            self, name: str, height: int, age: int, color: str, points: int
            ) -> None:
        super().__init__(name, height, age, color)
        self.points = points
        self.plant_type = "prize"


class GardenManager:
    total_managed = 0

    def __init__(self, owner) -> None:
        self.owner = owner
        self.plants = []
        self.analytics = self.GardenStats()
        GardenManager.total_managed += 1

    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")

    def generate_report(self) -> None:
        print("Plants in garden:")
        count = 0
        for _ in self.plants:
            count += 1

        for i in range(count):
            plant = self.plants[i]

            report_line = f"- {plant.name}: {plant.height}cm"

            if plant.plant_type in ["flowering", "prize"]:
                report_line += f", {plant.color} flowers (blooming)"
            if plant.plant_type in ["prize"]:
                report_line += f", Prize points: {plant.points}"
            print(report_line)

        reg, flow, prz = self.analytics.calculate(self.plants)
        print()
        print(f"Plants added: {count}, Total growth: {count}cm")
        print(f"Plant types: {reg} regular, {flow} "
              f"flowering, {prz} prize flowers")

    @staticmethod
    def validate_score(score) -> int:
        if score > 0:
            return score
        else:
            return 0

    @classmethod
    def create_garden_network(cls) -> list:
        alice = cls("Alice")
        bob = cls("Bob")
        return [alice, bob]

    class GardenStats:
        def calculate(self, plants) -> tuple:
            regular = 0
            flowering = 0
            prize = 0

            for p in plants:
                name = p.__class__.__name__
                if name == "PrizeFlower":
                    prize += 1
                elif name == "FloweringPlant":
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===")
    alice_manager, _ = GardenManager.create_garden_network()

    oak = Plant("Oak Tree", 100, 30)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 30, "yellow", 10)
    print()
    alice_manager.add_plant(oak)
    alice_manager.add_plant(rose)
    alice_manager.add_plant(sunflower)
    print()
    alice_manager.help_all_grow()
    print()
    print("=== Alice's Garden Report ===")
    alice_manager.generate_report()
    print()
    is_valid = GardenManager.validate_score(alice_manager.plants[0].height) > 0
    print(f"Height validation test: {is_valid}")
    alice_score = GardenManager.validate_score(218)
    bob_score = GardenManager.validate_score(92)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_managed}")


if __name__ == "__main__":
    ft_garden_analytics()

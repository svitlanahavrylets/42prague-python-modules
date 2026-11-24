class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value}days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def display_status(self) -> None:
        print(f"Current plant: {self.name} ({self._height}cm, "
              f"{self._age}days)")


def garden_security():
    print("=== Garden Security System ===")
    Rose = SecurePlant("Rose")

    Rose.set_height(25)
    Rose.set_age(30)
    print()
    Rose.set_height(-5)
    print()
    Rose.display_status()


if __name__ == "__main__":
    garden_security()

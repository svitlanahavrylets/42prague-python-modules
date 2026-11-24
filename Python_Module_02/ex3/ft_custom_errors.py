#!/usr/bin/env python

class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        error_name = e.__class__.__name__
        print(f"Caught {error_name}: {e}")
    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        error_name = e.__class__.__name__
        print(f"Caught {error_name}: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        parent_error_name = e.__class__.__bases__[0].__name__
        print(f"Caught {parent_error_name}: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        parent_error_name = e.__class__.__bases__[0].__name__
        print(f"Caught {parent_error_name}: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_custom_errors()

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    print(" base:")

    my_monster = factory.create_base()
    print(my_monster.describe())
    print(my_monster.attack())
    if isinstance(my_monster, HealCapability):
        print(my_monster.heal())

    print(" evolved:")
    my_better_monster = factory.create_evolved()
    print(my_better_monster.describe())
    print(my_better_monster.attack())
    if isinstance(my_better_monster, HealCapability):
        print(my_better_monster.heal())


def test_transform() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print(" base:")
    my_monster = factory.create_base()
    print(my_monster.describe())
    print(my_monster.attack())
    if isinstance(my_monster, TransformCapability):
        print(my_monster.transform())
        print(my_monster.attack())
        print(my_monster.revert())

    print(" evolved:")
    my_better_monster = factory.create_evolved()
    print(my_better_monster.describe())
    print(my_better_monster.attack())
    if isinstance(my_better_monster, TransformCapability):
        print(my_better_monster.transform())
        print(my_better_monster.attack())
        print(my_better_monster.revert())


def main() -> None:
    test_healing()
    print()
    test_transform()


if __name__ == "__main__":
    main()

from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    my_monster = factory.create_base()
    my_better_monster = factory.create_evolved()

    print(my_monster.describe())
    print(my_monster.attack())
    print(my_better_monster.describe())
    print(my_better_monster.attack())


def test_battle(
        flame_factory: CreatureFactory,
        aqua_factory: CreatureFactory
        ) -> None:
    print("Testing battle")
    monster1 = flame_factory.create_base()
    monster2 = aqua_factory.create_base()

    print(monster1.describe())
    print(" vs.")
    print(monster1.describe())
    print(" fight!")
    print(monster1.attack())
    print(monster2.attack())


def main() -> None:

    flame_factory = FlameFactory()
    test_factory(flame_factory)
    print()
    aqua_factory = AquaFactory()
    test_factory(aqua_factory)
    print()
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()

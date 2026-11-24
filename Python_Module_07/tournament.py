from typing import List, Tuple
from ex2 import (
    AggressiveStrategy,
    AquaFactory,
    BattleStrategy,
    CreatureFactory,
    DefensiveStrategy,
    FlameFactory,
    HealingCreatureFactory,
    InvalidStrategyError,
    NormalStrategy,
    TransformCreatureFactory,
)


def run_tournament(
    opponents: List[Tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """Run a tournament between opponents using their strategies."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            f1, s1 = opponents[i]
            f2, s2 = opponents[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            print("\n* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggr_strategy = AggressiveStrategy()
    def_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament([
        (flame_factory, normal_strategy),
        (heal_factory, def_strategy)
        ])
    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    run_tournament([
        (flame_factory, aggr_strategy),
        (heal_factory, def_strategy)
        ])
    print()

    print("Tournament 2 (multiple)")
    print(
        "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
    )
    run_tournament([
        (aqua_factory, normal_strategy),
        (heal_factory, def_strategy),
        (trans_factory, aggr_strategy)
        ])


if __name__ == "__main__":
    main()

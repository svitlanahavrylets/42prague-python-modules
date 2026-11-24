import random
from typing import List, Set


def gen_player_achievements(all_achievements: List[str]) -> Set[str]:
    num_achievements = random.randint(2, 9)
    player_list = random.sample(all_achievements, num_achievements)
    return set(player_list)


def main() -> None:
    all_achievements_list = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer',
        'Strategist', 'Unstoppable', 'Speed Runner', 'Survivor',
        'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Hidden Path Finder'
    ]
    all_possible_sets = set(all_achievements_list)

    alice = gen_player_achievements(all_achievements_list)
    bob = gen_player_achievements(all_achievements_list)
    charlie = gen_player_achievements(all_achievements_list)
    dylan = gen_player_achievements(all_achievements_list)

    print("=== Achievement Tracker System ===")
    print()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    distinct_achievements = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {distinct_achievements}")
    print()
    common_achievements = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common_achievements}")
    print()
    print(
        f"Only Alice has: "
        f"{alice.difference(bob.union(charlie, dylan))}")
    print(
        f"Only Bob has: "
        f"{bob.difference(alice.union(charlie, dylan))}")
    print(
        f"Only Charlie has: "
        f"{charlie.difference(alice.union(bob, dylan))}")
    print(
        f"Only Dylan has: "
        f"{dylan.difference(alice.union(bob, charlie))}")

    print(f"Alice is missing: {all_possible_sets.difference(alice)}")
    print(f"Bob is missing: {all_possible_sets.difference(bob)}")
    print(f"Charlie is missing: {all_possible_sets.difference(charlie)}")
    print(f"Dylan is missing: {all_possible_sets.difference(dylan)}")


if __name__ == "__main__":
    main()

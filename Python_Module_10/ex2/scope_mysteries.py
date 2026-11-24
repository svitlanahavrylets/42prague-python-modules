from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    current_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal current_power

        current_power += amount
        return current_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def sword_factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return sword_factory


def memory_vault() -> dict[str, Callable]:
    vault: dict = {}

    def store(key: str, value: int | str) -> None:
        vault[key] = value

    def recall(key: str) -> int | str:
        if key in vault:
            return vault[key]
        return "Memory not found"
    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    counter_a = mage_counter()
    counter_b = mage_counter()

    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    ac = spell_accumulator(100)
    print(f"Base 100, add 20: {ac(20)}")
    print(f"Base 100, add 30: {ac(30)}")

    print("\nTesting enchantment factory...")
    flaming_enchant = enchantment_factory("Flaming")
    frozen_enchant = enchantment_factory("Frozen")
    print(f"{flaming_enchant('Shield')}")
    print(f"{frozen_enchant('Sword')}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()

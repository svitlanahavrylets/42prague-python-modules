from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combines two spells into a single funcreturning a tuple of results."""
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return res1, res2

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplifies base spell's power by multiplying it before execution."""
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Casts spell only if condition function returns True."""
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    """Creates a sequence function that executes all spells in order."""
    def sequence_spell(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results

    return sequence_spell


def fireball(target: str, power: int) -> str:
    """Fireball spell implementation."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Heal spell implementation."""
    return f"Heal restores {target} for {power} HP"


def is_powerful_enough(target: str, power: int) -> bool:
    """Condition check for casting spells."""
    _ = target
    return power >= 20


def main() -> None:
    """Main function demonstrating higher-order spell functions."""
    test_values = [25, 7, 20]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    target = test_targets[0]
    base_power = test_values[1]
    high_power = test_values[0]

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined(target, base_power)
    print(f"Combined spell result: {res1}, {res2}\n")

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original_res = fireball(target, base_power)
    amplified_res = mega_fireball(target, base_power)
    print(f"Original: {original_res}")
    print(f"Amplified: {amplified_res}\n")

    print("Testing conditional caster...")
    conditional_fireball = conditional_caster(is_powerful_enough, fireball)
    print(
        f"Power {base_power} on {test_targets[1]}: "
        f"{conditional_fireball(test_targets[1], base_power)}"
    )
    print(
        f"Power {high_power} on {target}: "
        f"{conditional_fireball(target, high_power)}\n"
    )

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    seq_results = sequence(test_targets[2], test_values[2])
    for res in seq_results:
        print(f"- {res}")


if __name__ == "__main__":
    main()

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Returns allowed ingredients for dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Records or rejects a dark spell."""
    val_result = validate_ingredients(ingredients)
    if "VALID" in val_result:
        return f"Spell recorded: {spell_name} ({val_result})"
    return f"Spell rejected: {spell_name} ({val_result})"

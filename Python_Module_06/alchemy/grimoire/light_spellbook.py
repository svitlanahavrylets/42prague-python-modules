from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Returns allowed ingredients for light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Records or rejects a light spell."""
    val_result = validate_ingredients(ingredients)
    if "VALID" in val_result:
        return f"Spell recorded: {spell_name} ({val_result})"
    return f"Spell rejected: {spell_name} ({val_result})"

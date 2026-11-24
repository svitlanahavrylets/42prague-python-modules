from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    """Brews a healing potion using earth and air elements."""
    earth = create_earth()
    air = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'."


def strength_potion() -> str:
    """Brews a strength potion using fire and water elements."""
    fire = create_fire()
    water = create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'."

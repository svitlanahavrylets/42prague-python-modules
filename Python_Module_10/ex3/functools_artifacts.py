import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire': functools.partial(base_enchantment, power=50, element='fire'),
        'ice': functools.partial(base_enchantment, power=50, element='ice'),
        'lightning': functools.partial(
            base_enchantment, power=50, element='lightning'
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell: Any) -> str:
        _ = spell
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    return (
        f"{element.capitalize()} enchantment ({power} power) cast on {target}"
    )


def main() -> None:
    print("Testing spell reducer...")
    spell_powers = [24, 40, 15, 14, 21, 28]
    operations = ['add', 'multiply', 'max', 'min']

    for op in operations:
        res = spell_reducer(spell_powers, op)
        print(f"{op.capitalize()}: {res}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"](target="Dragon"))
    print(enchanters["ice"](target="Goblin"))
    print(enchanters["lightning"](target="Chulk"))

    print("\nTesting memoized fibonacci...")
    fib_tests = [0, 1, 10, 15, 19]
    for n in fib_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()

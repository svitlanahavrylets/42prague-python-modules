from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    res = dark_spell_record("Darkness", "Bats and frogs")
    print(f"Testing record dark spell: {res}")


if __name__ == "__main__":
    main()

import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}")


if __name__ == "__main__":
    main()

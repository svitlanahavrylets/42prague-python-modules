def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']

    total = sum(map(lambda x: x['power'], mages))
    average = round(total / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': average
    }


def main() -> None:

    artifacts_data = [
        {'name': 'Fire Staff', 'power': 63, 'type': 'armor'},
        {'name': 'Storm Crown', 'power': 80, 'type': 'armor'},
        {'name': 'Storm Crown', 'power': 70, 'type': 'accessory'},
        {'name': 'Earth Shield', 'power': 106, 'type': 'relic'}
    ]
    mages_data = [
        {'name': 'Jordan', 'power': 85, 'element': 'shadow'},
        {'name': 'Zara', 'power': 92, 'element': 'water'},
        {'name': 'Riley', 'power': 52, 'element': 'light'},
        {'name': 'Kai', 'power': 72, 'element': 'earth'},
        {'name': 'Luna', 'power': 78, 'element': 'earth'},
        {'name': 'Lunat', 'power': 81, 'element': 'water'}
    ]
    spells_data = ['meteor', 'shield', 'heal', 'blizzard']

    print("Testing artifact sorter...")
    print(f"{artifact_sorter(artifacts_data)}\n")

    print("Testing power filter...")
    print(f"Filtered mages: {power_filter(mages_data, 75)}\n")

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells_data)))

    print("\nTesting mage stats...")
    print(mage_stats(mages_data))


if __name__ == "__main__":
    main()

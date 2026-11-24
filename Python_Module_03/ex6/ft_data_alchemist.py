import random


def main():
    print("=== Game Data Alchemist ===")
    print()
    initial_players = ['Alice', 'bob', 'Charlie', 'dylan',
                       'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_players}")

    all_capitalized = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized = [name for name in initial_players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")
    print()
    score_dict = {name: random.randint(10, 1000) for name in all_capitalized}
    print(f"Score dict: {score_dict}")

    average_score = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average_score}")

    high_scores = {
        name: score
        for name, score in score_dict.items()
        if score > average_score
        }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

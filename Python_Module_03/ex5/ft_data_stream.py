import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move',
               'climb', 'swim', 'use', 'release']

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
        event_list: list
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        random_index = random.randint(0, len(event_list) - 1)

        selected_event = event_list.pop(random_index)

        print(f"Got event from list: {selected_event}")
        print(f"Remains in list: {event_list}")

        yield selected_event


def main():
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        event = next(stream)
        player, action = event
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = []
    for _ in range(10):
        ten_events.append(next(stream))

    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        pass


if __name__ == "__main__":
    main()

#!/usr/bin/env python

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    input_data_1 = "25"
    print(f"Input data is '{input_data_1}'")
    try:
        temp = input_temperature(input_data_1)
        print(f"Temperature is now {temp}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    input_data_2 = "abc"
    print(f"Input data is '{input_data_2}'")
    try:
        temp = input_temperature(input_data_2)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

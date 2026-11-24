#!/usr/bin/env python

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    if temp < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    else:
        return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
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

    input_data_3 = "100"
    print(f"Input data is '{input_data_3}'")
    try:
        temp = input_temperature(input_data_3)
        print(f"Temperature is now {temp}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    input_data_4 = "-50"
    print(f"Input data is '{input_data_4}'")
    try:
        temp = input_temperature(input_data_4)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

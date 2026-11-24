#!/usr/bin/env python

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 5
    else:
        return


def test_error_types() -> None:

    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
            if operation_number == 4:
                print("Operation completed successfully")
        except (ValueError,
                TypeError,
                ZeroDivisionError,
                FileNotFoundError) as e:
            error_name = e.__class__.__name__
            print(f"Caught {error_name}: {e}")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()

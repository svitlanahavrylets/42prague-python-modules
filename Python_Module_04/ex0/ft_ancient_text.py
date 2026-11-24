import sys


def get_content() -> None:
    arrArg = sys.argv
    lenArg = len(arrArg)

    if lenArg != 2:
        print(f"Usage: {arrArg[0]} <file>")
        return

    filename = arrArg[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        print("---")
        print()
        print(content)
        print()
        print("---")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if f is not None:
            f.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    get_content()

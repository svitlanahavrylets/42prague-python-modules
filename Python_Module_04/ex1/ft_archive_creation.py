import sys


def get_content() -> None:
    arrArg = sys.argv
    lenArg = len(arrArg)

    if lenArg != 2:
        print(f"Usage: {arrArg[0]} <file>")
        return

    filename = arrArg[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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
        return
    finally:
        if f is not None:
            f.close()
            print(f"File '{filename}' closed.")

    print()
    print("Transform data:")
    print("---")
    print()
    lines = content.splitlines()
    tranformed_lines = [(line + "#") for line in lines]
    new_content = "\n".join(tranformed_lines) + "\n"
    print(new_content)
    print()
    print("---")

    new_filename = input("Enter new file name (or empty): ").strip()
    if not new_filename:
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")

        out_f = None
        try:
            out_f = open(new_filename, "w", encoding="utf-8")
            out_f.write(new_content)
            print(f"Data saved in file '{new_filename}'")
        except Exception as e:
            print(f"Error saving file '{new_filename}': {e}")
        finally:
            if out_f is not None:
                out_f.close()


if __name__ == "__main__":
    get_content()

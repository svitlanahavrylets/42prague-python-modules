import sys


def get_arg() -> None:
    arrArg = sys.argv
    lenArg = len(arrArg)

    print("=== Command Quest ===")
    print(f'Program name: {arrArg[0]}')

    if lenArg > 1:
        print(f"Arguments received: {lenArg - 1}")
        for i in range(1, lenArg):
            print(f"Argument {i}: {arrArg[i]}")
    else:
        print("No arguments provided!")
    print(f'Total arguments: {lenArg}')


if __name__ == "__main__":
    get_arg()

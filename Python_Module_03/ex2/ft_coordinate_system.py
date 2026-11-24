import math
from typing import Tuple


def get_player_pos() -> Tuple[float, float, float]:
    while True:
        req = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = req.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords = []
        success = True
        for part in parts:
            clean_part = part.strip()
            try:
                coords.append(float(clean_part))
            except ValueError:
                print(
                    f"Error on parameter '{clean_part}': "
                    f"could not convert string to float: '{clean_part}'"
                    )
                success = False
                break
        if success:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1: Tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_to_center = math.sqrt((pos1[0])**2 + (pos1[1])**2 + (pos1[2])**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")
    print()

    print("Get a second set of coordinates")
    pos2: Tuple[float, float, float] = get_player_pos()
    dx: float = pos2[0] - pos1[0]
    dy: float = pos2[1] - pos1[1]
    dz: float = pos2[2] - pos1[2]
    dist_between: float = math.sqrt(dx**2 + dy**2 + dz**2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()

import sys


def main():
    print("=== Inventory System Analysis ===")
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        pass

    inventory = {}
    insertion_order = []
    for arg in arguments:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, qty_str = arg.split(':', 1)

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory[item] = quantity
        insertion_order.append(item)

    print(f"Got inventory: {inventory}")

    items_list = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item in insertion_order:
        qty = inventory[item]

        if total_qty > 0:
            percentage = qty / total_qty * 100
        else:
            percentage = 0.0
        print(f"Item {item} represents {round(percentage, 1)}%")

    if inventory:
        most_abundant = insertion_order[0]
        least_abundant = insertion_order[0]

        for item in insertion_order:
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item

            if inventory[item] < inventory[least_abundant]:
                least_abundant = item

        print(f"Item most abundant: "
              f"{most_abundant} with quantity {inventory[most_abundant]}")
        print(f"Item least abundant: "
              f"{least_abundant} with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

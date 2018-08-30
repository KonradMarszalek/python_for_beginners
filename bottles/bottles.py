for bottle_number in range(99, 0, -1):
    bottle_number_minus = bottle_number - 1
    print(
        f"{bottle_number} bottles of beer on the wall, "
        f"{bottle_number} bottles of beer. "
        f"Take one down and pass it around - "
        f"{bottle_number_minus} bottles of beer on the wall.")

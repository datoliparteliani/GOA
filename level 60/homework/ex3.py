def feast(beast, dish):
    beast_first, beast_last = beast[0], beast[-1]
    dish_first, dish_last = dish[0], dish[-1]
    return beast_first == dish_first and beast_last == dish_last
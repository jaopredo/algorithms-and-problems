from math import floor


def least_coins(value: int, monetary_system: list[int]):
    if value == 0:
        return 0
    greatest_coin = monetary_system[0]
    n = floor(value/greatest_coin)
    monetary_system.pop(0)
    return n + least_coins(value-n*greatest_coin, monetary_system)


print(least_coins(37, [25, 10, 5, 1]))
print(least_coins(63, [50, 20, 10, 1]))

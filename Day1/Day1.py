import numpy as np


def fuel(mass):
    return np.floor(mass / 3) - 2


def fuel_recursive(mass):
    if (fuel(mass)) <= 0:
        return 0
    elif (fuel(fuel(mass)) <= 0):
        return fuel(mass)
    else:
        return fuel(mass) + fuel(fuel(mass)) + fuel_recursive(fuel(fuel(mass)))


with open("Day1\\input1.txt", "r") as f:
    masses = [int(x.strip()) for x in f.readlines()]

    total_fuel = 0
    total_fuel_recursive = 0

    for mass in masses:
        total_fuel += fuel(mass)
        total_fuel_recursive += fuel_recursive(mass)

    print("Answer to part 1: " + str(total_fuel))  # Solution to part 1
    print("Answer to part 2: " + str(total_fuel_recursive))  # Solution to part 2


# Examples from the problem
# print(fuel_recursive(14))
# print(fuel_recursive(1969))
# print(fuel_recursive(100756))

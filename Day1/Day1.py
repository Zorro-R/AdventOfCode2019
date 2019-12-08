import numpy as np


def fuel(mass):
    return np.floor(mass / 3) - 2


def fuel_recursive(mass):
    #fuel_required = 0
    # print(fuel(mass))
    # print(fuel(fuel(mass)))
    #skurr = input("Pause")
    if (fuel(fuel(mass)) <= 0):  # Base case
        #print("Base case" + str(fuel(mass)))
        return fuel(mass)
    else:  # Recursive case
        #print("Recursive case: " + str((fuel(mass) + fuel_recursive(fuel(fuel(mass))))))
        return fuel(mass) + fuel(fuel(mass)) + fuel_recursive(fuel(fuel(mass)))


with open("input1.txt", "r") as f:
    masses = [int(x.strip()) for x in f.readlines()]
    print(masses)

    total_fuel = 0
    total_fuel_recursive = 0

    for mass in masses:
        total_fuel += fuel(mass)
        total_fuel_recursive += fuel_recursive(mass)

    print("Answer to part 1: " + str(total_fuel))  # Solution to part 1
    print("Answer to part 2: " + str(total_fuel_recursive))  # Solution to part 2


# These all work but the answer is still wrong :/
# print(fuel_recursive(14))
# print(fuel_recursive(1969))
# print(fuel_recursive(100756))

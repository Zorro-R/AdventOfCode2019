import numpy as np

# fuel = floor(mass / 3) - 2

with open("Input1.txt", "r") as f:
    masses = f.readlines()


    total_fuel = 0

    for mass in masses:
        fuel_required = np.floor(int(mass) / 3) - 2
        total_fuel += fuel_required

    print(total_fuel)
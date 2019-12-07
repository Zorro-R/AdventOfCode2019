import numpy as np


def run_intcode(intcode):
    for i in range(0, len(intcode), 4):
        code = intcode[i]
        # Check operation type
        if code == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + \
                intcode[intcode[i+2]]
        elif code == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * \
                intcode[intcode[i+2]]

        elif code == 99:
            return(intcode[0])


with open("Input2.txt", "r") as f:
    intcode_static = [int(x) for x in f.readlines()[0].split(",")]

    # Make a copy of intcode to be modified
    intcode_part1 = np.copy(intcode_static)
    intcode_part1[1], intcode_part1[2] = 12, 2  # Mofify noun and verb

    print(run_intcode(intcode_part1))  # Solution to part 1

    # Solution to part 2
    for noun in range(100):
        for verb in range(100):
            # Make a copy of intcode to be modified
            intcode_part2 = np.copy(intcode_static)
            # Modify noun and verb
            intcode_part2[1], intcode_part2[2] = noun, verb

            if run_intcode(intcode_part2) == 19690720:
                print(100 * noun + verb)
                break

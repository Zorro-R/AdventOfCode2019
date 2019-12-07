def run_intcode(intcode):
    for i, code in enumerate(intcode):
        # Is code an operation
        if i % 4 == 0:
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
    intcode = [int(x) for x in f.readlines()[0].split(",")]

    intcode[1], intcode[2] = 12, 2

    print(run_intcode(intcode))  # Solution to part A

#print(run_intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]))

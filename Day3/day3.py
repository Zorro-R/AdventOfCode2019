with open("input3.txt", "r") as f:
    wire_instructions = f.readlines()

    wires = []
    for wire_instruction in wire_instructions:

        wire_path = []
        x = 0
        y = 0

        for instruction in wire_instruction.split(","):
            # If the wire goes up
            if instruction[0] == "U":
                for i in range(int(instruction[1:])):
                    wire_path.append([x, y + i])
                y += int(instruction[1:])
            # If the wire goes down
            if instruction[0] == "D":
                for i in range(int(instruction[1:])):
                    wire_path.append([x, y - i])
                y -= int(instruction[1:])
            # If the wire goes right
            if instruction[0] == "R":
                for i in range(int(instruction[1:])):
                    wire_path.append([x + i, y])
                x += int(instruction[1:])
            # If the wire goes left
            if instruction[0] == "L":
                for i in range(int(instruction[1:])):
                    wire_path.append([x - i, y])
                x -= int(instruction[1:])

        wires.append(wire_path)

    # Since there are only two wires we only need to check the intersections once
    intersections = []
    for wire_coordinate in wires[0]:
        # Ensure to exclude the starting point
        if wire_coordinate in wires[1] and wire_coordinate != [0, 0]:
            intersections.append(wire_coordinate)

    # Check for the smallest Manhattan distance of all intersection points
    def manhattan_distance(wire_coordinate):
        return abs(wire_coordinate[0]) + abs(wire_coordinate[1])

    # Assume the closest intersection is infinitely far away
    closest_intersection = float("inf")
    for intersection in intersections:
        # If a closer intersection is found assume that to be the new closest intersection
        if manhattan_distance(intersection) < closest_intersection:
            closest_intersection = manhattan_distance(intersection)

    print(closest_intersection)  # Solution to part 1

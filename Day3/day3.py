with open("input3.txt", "r") as f:
    wire_instructions = f.readlines()
    # wire_instructions = [
    #     "R75,D30,R83,U83,L12,D49,R71,U7,L72",
    #     "U62,R66,U55,R34,D71,R55,D58,R83"]

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

    # Takes a wire and an intersection and returns the number of steps it takes that wire to get to that intersection
    def steps_to_intersection(intersection, wires):
        return wires[0].index(intersection) + wires[1].index(intersection)

    # Assume the closest intersection is infinitely far away
    closest_intersection = float("inf")
    fastest_intersection = float("inf")
    for intersection in intersections:
        # If a closer intersection is found assume that to be the new closest intersection
        dist_to_intersec = manhattan_distance(intersection)
        if dist_to_intersec < closest_intersection:
            closest_intersection = dist_to_intersec

        # For part 2
        fast_dist_to_intersec = steps_to_intersection(intersection, wires)
        if fast_dist_to_intersec < fastest_intersection:
            fastest_intersection = fast_dist_to_intersec

    print(closest_intersection)  # Solution to part 1
    print(fastest_intersection)  # Solution to part 2

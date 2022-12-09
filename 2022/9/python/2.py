
no_knots = 10

knots = [[0,0] for _ in range(no_knots)]
head = knots[0]
tail = knots[-1]
tail_visited_coordinates = {f"0,0": 1}

while True:
    try:
        motion = input().split(" ")
        direction = motion[0]
        steps = int(motion[1])

        for step in range(steps):
            if direction == "U":
                head[0] -= 1
            elif direction == "D":
                head[0] += 1
            elif direction == "L":
                head[1] -= 1
            elif direction == "R":
                head[1] += 1

            for i in range(1, no_knots):
                if knots[i][1] - knots[i-1][1] < -1:    # knot is on the right of previous knot by more than 1
                    knots[i][1] += 1
                    if knots[i][0] < knots[i-1][0]:     # knot is above previous knot
                        knots[i][0] += 1
                    elif knots[i][0] > knots[i-1][0]:   # knot is below previous knot
                        knots[i][0] -= 1

                elif knots[i][1] - knots[i-1][1] > 1:   # knot is on the left of previous knot by more than 1
                    knots[i][1] -= 1
                    if knots[i][0] < knots[i-1][0]:     # knot is above previous knot
                        knots[i][0] += 1
                    elif knots[i][0] > knots[i-1][0]:   # knot is below previous knot
                        knots[i][0] -= 1

                elif knots[i][0] - knots[i-1][0] > 1:   # knot is below previous knot by more than 1
                    knots[i][0] -= 1
                    if knots[i][1] < knots[i-1][1]:     # knot is on the left of previous knot
                        knots[i][1] += 1
                    elif knots[i][1] > knots[i-1][1]:   # knot is on the right of previous knot
                        knots[i][1] -= 1

                elif knots[i][0] - knots[i-1][0] < -1:  # knot is above previous knot by more than 1
                    knots[i][0] += 1
                    if knots[i][1] < knots[i-1][1]:     # knot is on the left of previous knot
                        knots[i][1] += 1
                    elif knots[i][1] > knots[i-1][1]:   # knot is on the right of previous knot
                        knots[i][1] -= 1

            try:
                tail_visited_coordinates[f"{tail[0]},{tail[1]}"] += 1
            except KeyError:
                tail_visited_coordinates[f"{tail[0]},{tail[1]}"] = 1

    except EOFError:
        break

print(len(tail_visited_coordinates.keys()))

head = [0, 0]
tail = [0, 0]
tail_visited_coordinates = {f"0,0": 1}

while True:
    try:
        motion = input().split(" ")
        direction = motion[0]
        steps = int(motion[1])

        for step in range(steps):
            if direction == "U":
                head[0] -= 1
                if tail[0] - head[0] > 1:  # tail is below head by more than 1
                    tail[0] -= 1
                    if tail[1] < head[1]:  # tail is on the left of head
                        tail[1] += 1
                    elif tail[1] > head[1]:  # tail is on the right of head
                        tail[1] -= 1

            elif direction == "D":
                head[0] += 1
                if tail[0] - head[0] < -1:  # tail is above head by more than 1
                    tail[0] += 1
                    if tail[1] < head[1]:  # tail is on the left of head
                        tail[1] += 1
                    elif tail[1] > head[1]:  # tail is on the right of head
                        tail[1] -= 1

            elif direction == "L":
                head[1] -= 1
                if tail[1] - head[1] > 1:  # tail is on the right of head by more than 1
                    tail[1] -= 1
                    if tail[0] < head[0]:  # tail is above head
                        tail[0] += 1
                    elif tail[0] > head[0]:  # tail is below head
                        tail[0] -= 1

            elif direction == "R":
                head[1] += 1
                if tail[1] - head[1] < -1:  # tail is on the left of head by more than 1
                    tail[1] += 1
                    if tail[0] < head[0]:  # tail is above head
                        tail[0] += 1
                    elif tail[0] > head[0]:  # tail is below head
                        tail[0] -= 1

            try:
                tail_visited_coordinates[f"{tail[0]},{tail[1]}"] += 1
            except KeyError:
                tail_visited_coordinates[f"{tail[0]},{tail[1]}"] = 1

    except EOFError:
        break

print(len(tail_visited_coordinates.keys()))

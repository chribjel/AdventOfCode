sand_source = (500, 0)
deepest_y = 0
floor_depth = 0
rocks = set()


def read_input():
    global deepest_y
    while True:
        try:
            rock_path = input().split(" -> ")
            rock_path = [
                (int(x.split(",")[0]), int(x.split(",")[1])) for x in rock_path
            ]
            for i in range(len(rock_path) - 1):
                x_diff = rock_path[i + 1][0] - rock_path[i][0]
                y_diff = rock_path[i + 1][1] - rock_path[i][1]

                if x_diff != 0:
                    for x in range(
                        0, x_diff + (x_diff // abs(x_diff)), x_diff // abs(x_diff)
                    ):
                        rocks.add((rock_path[i][0] + x, rock_path[i][1]))
                        if rock_path[i][1] > deepest_y:
                            deepest_y = rock_path[i][1]
                elif y_diff != 0:
                    for y in range(
                        0, y_diff + (y_diff // abs(y_diff)), y_diff // abs(y_diff)
                    ):
                        rocks.add((rock_path[i][0], rock_path[i][1] + y))
                        if rock_path[i][1] + y > deepest_y:
                            deepest_y = rock_path[i][1] + y
        except EOFError:
            break


def fill_cave_with_sand():
    global floor_depth
    sand_count = 0
    current_sand_pos = sand_source
    while True:

        if current_sand_pos[1] + 1 >= floor_depth:
            rocks.add(current_sand_pos)
            current_sand_pos = sand_source
            sand_count += 1
            continue

        possible_new_sand_pos = [
            (current_sand_pos[0], current_sand_pos[1] + 1),
            (current_sand_pos[0] - 1, current_sand_pos[1] + 1),
            (current_sand_pos[0] + 1, current_sand_pos[1] + 1),
        ]

        for pos in possible_new_sand_pos:
            if pos not in rocks:
                current_sand_pos = pos
                break
        else:  # no new sand pos found
            rocks.add(current_sand_pos)
            sand_count += 1
            if current_sand_pos == sand_source:
                break
            current_sand_pos = sand_source
            continue

    return sand_count


read_input()
floor_depth = deepest_y + 2
print(fill_cave_with_sand())

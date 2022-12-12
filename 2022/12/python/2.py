from typing import List, Tuple


def start_and_end(matrix: List[str], start_symbol: str = "S", end_symbol: str = "E"):
    start = []
    end = None

    # find starting position
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == start_symbol:
                start.append((i, j))
                break
    # find end position
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == end_symbol:
                end = (i, j)
                break

    return start, end


def find_path_bfs(matrix: List[str], start: Tuple[int, int], end: Tuple[int, int]):
    # create a queue
    queue: List[Tuple[Tuple[int, int], int]] = [(start, 0)]
    # create a set of visited nodes
    visited = set()

    # while the queue is not empty
    while len(queue) > 0:
        # get the first item in the queue
        curr_idx, steps = queue.pop(0)

        # if we've already visited this position, continue
        if curr_idx in visited:
            continue

        # add current position to visited
        visited.add(curr_idx)

        # if we've reached the end, return the number of steps
        if curr_idx == end:
            return steps

        # get the current letter
        curr_letter = matrix[curr_idx[0]][curr_idx[1]]
        if curr_letter == "S":
            curr_letter = "a"

        # get the next possible positions
        next_pos = [
            (curr_idx[0] - 1, curr_idx[1]),  # up
            (curr_idx[0] + 1, curr_idx[1]),  # down
            (curr_idx[0], curr_idx[1] - 1),  # left
            (curr_idx[0], curr_idx[1] + 1),  # right
        ]

        # for each next position
        for pos in next_pos:
            # if the next position is in bounds
            if (
                0 <= pos[0] < len(matrix)
                and 0 <= pos[1] < len(matrix[0])
                and pos not in visited
            ):
                # get the next letter
                next_letter = matrix[pos[0]][pos[1]]
                # if the next letter is the same or one letter higher than the current letter
                if ord(next_letter) - ord(curr_letter) <= 1:
                    # add the next position to the queue
                    queue.append((pos, steps + 1))

    return None


m = []
while True:
    try:
        line = input()
        m.append(line)
    except EOFError:
        break

start, end = start_and_end(m)
startA, end = start_and_end(m, "a")
paths = []
if len(start) > 0 and len(startA) > 0 and end:
    paths.append(find_path_bfs(m, start[0], end))
    for s in startA:
        paths.append(find_path_bfs(m, s, end))

print(min(paths))

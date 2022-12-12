forest = []
scenic_scores = {}

while True:
    try:
        row = input()
        forest.append(row)
    except EOFError:
        break

for i in range(0, len(forest)):
    for j in range(0, len(forest[i])):

        tree = int(forest[i][j])
        scenic_scores[f"{i},{j}"] = 1

        east = 0
        for k in range(j + 1, len(forest[i])):
            east += 1
            if tree <= int(forest[i][k]):
                break
        scenic_scores[f"{i},{j}"] *= east

        south = 0
        for k in range(i + 1, len(forest)):
            south += 1
            if tree <= int(forest[k][j]):
                break
        scenic_scores[f"{i},{j}"] *= south

        west = 0
        for k in range(j - 1, -1, -1):
            west += 1
            if tree <= int(forest[i][k]):
                break
        scenic_scores[f"{i},{j}"] *= west

        north = 0
        for k in range(i - 1, -1, -1):
            north += 1
            if tree <= int(forest[k][j]):
                break
        scenic_scores[f"{i},{j}"] *= north


print(max(scenic_scores.values()))

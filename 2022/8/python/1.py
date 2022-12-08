
forest = []
visible_trees = []

while True:
    try:
        row = input()
        forest.append(row)
    except EOFError:
        break

for i in range(0, len(forest)):
    for j in range(0, len(forest[i])):
        if i == 0 or i == len(forest)-1 or j == 0 or j == len(forest[i])-1: # check if on edge
            visible_trees.append([i, j])
            continue

        tree = int(forest[i][j])

        for k in range(0, j):  # check row to the right
            if tree <= int(forest[i][k]): # tree not visible from this direction
                break
        else:
            visible_trees.append([i, j])
            continue

        for k in range(0, i):  # check column down
            if tree <= int(forest[k][j]): # tree not visible from this direction
                break
        else:
            visible_trees.append([i, j])
            continue

        for k in range(len(forest[i])-1, j, -1):   # check row to the left
            if tree <= int(forest[i][k]): # tree not visible from this direction
                break
        else:
            visible_trees.append([i, j])
            continue

        for k in range(len(forest)-1, i, -1):  # check column up
            if tree <= int(forest[k][j]): # tree not visible from this direction
                break
        else:
            visible_trees.append([i, j])
            continue


print(len(visible_trees))

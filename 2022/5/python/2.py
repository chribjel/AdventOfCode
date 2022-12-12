"""
        [F] [Q]         [Q]
[B]     [Q] [V] [D]     [S]
[S] [P] [T] [R] [M]     [D]
[J] [V] [W] [M] [F]     [J]     [J]
[Z] [G] [S] [W] [N] [D] [R]     [T]
[V] [M] [B] [G] [S] [C] [T] [V] [S]
[D] [S] [L] [J] [L] [G] [G] [F] [R]
[G] [Z] [C] [H] [C] [R] [H] [P] [D]
 1   2   3   4   5   6   7   8   9

"""
crates = [
    ["B", "S", "J", "Z", "V", "D", "G"],
    ["P", "V", "G", "M", "S", "Z"],
    ["F", "Q", "T", "W", "S", "B", "L", "C"],
    ["Q", "V", "R", "M", "W", "G", "J", "H"],
    ["D", "M", "F", "N", "S", "L", "C"],
    ["D", "C", "G", "R"],
    ["Q", "S", "D", "J", "R", "T", "G", "H"],
    ["V", "F", "P"],
    ["J", "T", "S", "R", "D"],
]


moving = False

while True:
    try:
        line = input()
        if not moving:
            if line == "":
                moving = True
                continue
        else:
            cmd = line.split(" ")
            qty = int(cmd[1])
            src = int(cmd[3]) - 1
            dst = int(cmd[5]) - 1

            for i in range(qty, 0, -1):
                crates[dst].insert(0, (crates[src].pop(i - 1)))

    except EOFError:
        break

for i in range(len(crates)):
    print(f"{crates[i][0]}", end="")

print()

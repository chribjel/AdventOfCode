x = 1
x_to_add = 0
cycles = 0
in_operation = False
should_add = False
crt = [[]]
crt_width = 40
crt_height = 6

while True:
    try:

        # start cycle
        if not in_operation:
            cmd = input().split(" ")
            if cmd[0] == "noop":
                cycles += 1
            elif cmd[0] == "addx":
                x_to_add = int(cmd[1], 10)
                cycles += 1
                in_operation = True
        elif in_operation:
            cycles += 1
            in_operation = False
            should_add = True

        if len(crt[-1]) == crt_width:
            crt.append([])
        if len(crt[-1]) == x or len(crt[-1]) == x + 1 or len(crt[-1]) == x - 1:
            crt[-1].append("#")
        else:
            crt[-1].append(".")

        if should_add:
            x += x_to_add
            should_add = False
        # end cycle

    except EOFError:
        break

for i in range(crt_height):
    for j in range(crt_width):
        print(crt[i][j], end="")
    print()

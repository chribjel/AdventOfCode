
forward = 0
down = 0
aim = 0

while True:
    try:
        cmd = input().split(" ")
        factor = int(cmd[1], 10)

        if cmd[0] == "forward":
            forward += factor
            down += aim * factor
        elif cmd[0] == "down":
            aim += factor
        elif cmd[0] == "up":
            aim -= factor

    except EOFError:
        break

print(forward * down)

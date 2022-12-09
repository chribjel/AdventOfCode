
forward = 0
down = 0

while True:
    try:
        cmd = input().split(" ")
        factor = int(cmd[1], 10)

        if cmd[0] == "forward":
            forward += factor
        elif cmd[0] == "down":
            down += factor
        elif cmd[0] == "up":
            down -= factor

    except EOFError:
        break

print(forward * down)

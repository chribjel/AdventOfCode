x = 1
x_to_add = 0
cycles = 0
cycles_to_check = [20, 60, 100, 140, 180, 220]
signal_strengths = []
in_operation = False
should_add = False

while True:
    try:
        # start cycle
        if not in_operation:
            cmd = input().split(" ")
            if cmd[0] == "noop":
                cycles += 1
            elif cmd[0] == "addx":
                x_to_add = int(cmd[1])
                cycles += 1
                in_operation = True
        elif in_operation:
            cycles += 1
            in_operation = False
            should_add = True

        if cycles in cycles_to_check:
            signal_strengths.append(x * cycles)
        if should_add:
            x += x_to_add
            should_add = False
        # end cycle

    except EOFError:
        break

print(signal_strengths)
print(sum(signal_strengths))

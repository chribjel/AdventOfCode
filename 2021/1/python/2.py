window = []
num_higher_than_prev = 0

while True:
    try:
        window.append(int(input()))

        if len(window) == 4:
            if sum(window[1:4]) > sum(window[0:3]):
                num_higher_than_prev += 1
            window.pop(0)

    except EOFError:
        break

print(num_higher_than_prev)

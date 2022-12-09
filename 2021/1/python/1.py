prev = None
num_higher_than_prev = 0

while True:
    try:
        curr = int(input())
        if prev is not None and curr > prev:
            num_higher_than_prev += 1
        prev = curr
    except EOFError:
        break

print(num_higher_than_prev)

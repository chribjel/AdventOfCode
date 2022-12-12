total = 0

while True:
    try:
        pair = input().split(",")
        pair1, pair2 = pair[0].split("-"), pair[1].split("-")
        pair1 = set(range(int(pair1[0], base=10), int(pair1[1], base=10) + 1))
        pair2 = set(range(int(pair2[0], base=10), int(pair2[1], base=10) + 1))

        if pair1.issubset(pair2) or pair2.issubset(pair1):
            total += 1
    except EOFError:
        break

print(total)

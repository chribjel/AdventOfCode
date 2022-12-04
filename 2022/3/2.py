
items = []

while True:
    try:
        backpack1, backpack2, backpack3 = input(), input(), input()

        for a in backpack1:
            for b in backpack2:
                for c in backpack3:
                    if a == b == c:
                        items.append(a)
                        break

                else:
                    continue
                break

            else:
                continue
            break

    except EOFError:
        break

total_priority = 0
# "a" is 1, "z" is 26
# "A" is 27, "Z" is 52
for item in items:
    total_priority += ord(item) - 96 if item.islower() else ord(item) - 38

print(total_priority)

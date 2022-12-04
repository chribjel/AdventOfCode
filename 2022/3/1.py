
items = []

while True:
    try:
        backpacks = input()

        backpack1, backpack2 = backpacks[0:len(backpacks)//2], backpacks[len(backpacks)//2:]

        for a in backpack1:
            for b in backpack2:
                if a == b:
                    items.append(a)
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

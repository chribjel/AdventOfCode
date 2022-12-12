highest = []
current = 0

while True:
    try:
        n = input()
        if n != "":
            n = int(n)
            current += n
        else:
            highest.append(current)
            current = 0
    except EOFError:
        highest.append(current)
        break

print(sum(sorted(highest, reverse=True)[0:3]))

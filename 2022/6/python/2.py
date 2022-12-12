buffer = input()

for i in range(len(buffer)):
    if len(set([char for char in buffer[i : i + 14]])) == 14:
        print(i + 14)
        break

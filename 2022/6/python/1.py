
buffer = input()

for i in range(len(buffer)):
    if len(set([char for char in buffer[i:i+4]])) == 4:
        print(i+4)
        break


dir_path = []
dir_sizes = {}
ls = False
update_size = 30000000
total_space = 70000000
total_size = 0

while True:
    try:
        line = input()

        lineList = line.split(" ")

        if lineList[0] == "$":
            ls = False
            if lineList[1] == "cd":
                if lineList[2] == "..":
                    dir_path.pop()
                elif lineList[2] == "/":
                    dir_path = []
                else:
                    dir_path.append(lineList[2])
            elif lineList[1] == "ls":
                ls = True
        elif ls:
            if lineList[0] != "dir":
                total_size += int(lineList[0])
                for i in range(len(dir_path)):
                    curr_dir = "/".join(dir_path[0:i+1])
                    if curr_dir in dir_sizes:
                        dir_sizes[curr_dir] += int(lineList[0])
                    else:
                        dir_sizes[curr_dir] = int(lineList[0])

    except EOFError:
        break

canditate_dirs = []
space_available = total_space - total_size
for key in dir_sizes:
    if dir_sizes[key] >= update_size-space_available:
        canditate_dirs.append([key, dir_sizes[key]])

canditate_dirs.sort(key=lambda x: x[1])


print(canditate_dirs[0][1])

def is_valid(left, right, i = 0):

    if isinstance(left, list):
        if isinstance(right, list):
            if len(left) == 0 and len(right) > 0:
                return True
            elif len(left) > 0 and len(right) == 0:
                return False
            elif len(left) == 0 and len(right) == 0:
                return None


            # both are lists
            for i in range(len(left)):
                try:
                    if is_valid(left[i], right[i], i) == False:
                        return False
                    elif is_valid(left[i], right[i], i) == None:
                        continue
                    return True
                except IndexError:
                    return False

            if len(left) < len(right):
                return True
            elif len(left) == len(right):
                return None
        else:
            return is_valid(left, [right])
    elif isinstance(right, list):
        return is_valid([left], right)
    else:
        if left > right:
            return False
        elif left == right:
            return None
        return True


valid_idxs = []
i = 1

while True:
    try:
        pair = eval(input()), eval(input())

        if is_valid(pair[0], pair[1]):
            valid_idxs.append(i)

        i += 1
        input()


    except EOFError:
        break

print(valid_idxs)
print(sum(valid_idxs))

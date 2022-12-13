class Packet:
    def __init__(self, list):
        self.list = list

    def __lt__(self, other):
        return is_valid(self.list, other.list) == True

    def __gt__(self, other):
        return is_valid(other.list, self.list) == False

    def __eq__(self, other):
        return is_valid(self.list, other.list) == None


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

divider1 = Packet([[2]])
divider2 = Packet([[6]])

packets = [divider1, divider2]

while True:
    try:
        pair = eval(input()), eval(input())
        packets.append(Packet(pair[0]))
        packets.append(Packet(pair[1]))
        input()

    except EOFError:
        break

packets.sort()

print((packets.index(divider1)+1) * (packets.index(divider2)+1))

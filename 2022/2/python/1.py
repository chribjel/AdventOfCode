score = 0

my_shape = {"X": 1, "Y": 2, "Z": 3}
opponent_shape = {"A": 1, "B": 2, "C": 3}


def result(opp, me):
    if opponent_shape[opp] == my_shape[me]:
        return 3 + my_shape[me]
    elif my_shape[me] == 2 and opponent_shape[opp] == 1:
        return 6 + my_shape[me]
    elif my_shape[me] == 3 and opponent_shape[opp] == 2:
        return 6 + my_shape[me]
    elif my_shape[me] == 1 and opponent_shape[opp] == 3:
        return 6 + my_shape[me]
    else:
        return 0 + my_shape[me]


while True:
    try:
        n = input()
        score += result(n[0], n[2])
    except EOFError:
        break

print(score)

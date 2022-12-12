score = 0

decider = {"X": 0, "Y": 3, "Z": 6}
opponent_shape = {"A": 1, "B": 2, "C": 3}


def result(opp, me):
    if decider[me] == 0:
        return decider[me] + (
            opponent_shape[opp] - 1 if opponent_shape[opp] - 1 > 0 else 3
        )
    elif decider[me] == 3:
        return decider[me] + opponent_shape[opp]
    else:
        return decider[me] + (
            opponent_shape[opp] + 1 if opponent_shape[opp] + 1 < 4 else 1
        )


while True:
    try:
        n = input()
        score += result(n[0], n[2])
    except EOFError:
        break

print(score)

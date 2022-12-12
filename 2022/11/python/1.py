from math import floor, prod
from time import sleep


def read_monkeys():
    monkeys = []
    monkey = {}
    while True:
        try:
            monkey_input = input()
            if monkey_input.strip().startswith("Monkey "):
                monkey["inspected_items"] = 0

            elif monkey_input.strip().startswith("Starting items:"):
                monkey["items"] = list(
                    map(int, monkey_input.strip().split(":")[1].strip().split(","))
                )

            elif monkey_input.strip().startswith("Operation:"):
                fun = monkey_input.strip().split("=")[-1].strip()
                monkey["operation"] = (lambda f: lambda old: eval(f))(fun)

            elif monkey_input.strip().startswith("Test:"):
                true_monkey = int(input().split(" ")[-1])
                false_monkey = int(input().split(" ")[-1])
                divisible_by = int(monkey_input.strip().split(" ")[-1])

                monkey["divisible_by"] = (
                    lambda t, f, d: lambda worry: t if worry % d == 0 else f
                )(true_monkey, false_monkey, divisible_by)

            elif monkey_input == "":
                monkeys.append(monkey)
                monkey = {}
                continue

        except EOFError:
            monkeys.append(monkey)
            monkey = {}
            break

    return monkeys


monkeys = read_monkeys()


def factorize(n):
    factors = set()
    for i in range(2, n + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    return factors


for i in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            worry = item

            # inspection starts
            monkey["inspected_items"] += 1
            worry = monkey["operation"](worry)

            # inspection ends
            worry = floor(worry / 3)

            # monkey decides which monkey to send the item to
            to_monkey = monkey["divisible_by"](worry)

            monkeys[to_monkey]["items"].append(worry)

        monkey["items"] = []

# sort the monkey descending based on the number of inspected items
monkeys.sort(key=lambda monkey: monkey["inspected_items"], reverse=True)

print(monkeys[0]["inspected_items"] * monkeys[1]["inspected_items"])

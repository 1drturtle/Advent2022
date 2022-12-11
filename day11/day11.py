from aocd import submit, data
from collections import namedtuple

EMPTY = object()
solution_one, solution_two = [EMPTY, EMPTY]
# grab data (Cached)
puzzle_data = data

# puzzle_data = """
# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
# """.strip()
# -- code below --

monkey_strings = puzzle_data.split("\n\n")
inspect_count = [0 for _ in range(len(monkey_strings))]

Monkey = namedtuple(
    "Monkey", ["items", "operator", "op_amount", "div_by", "true", "false"]
)
monkeys: list[Monkey] = []


# parse monkeys
def parse_monkeys():
    MAX_VAL = 1
    for monkey in monkey_strings:
        monkey = [line.strip() for line in monkey.splitlines()[1:]]
        items = list(map(int, monkey[0][16:].split(", ")))
        operation = monkey[1][21:].split()
        div_by = int(monkey[2][19:])
        if_true = int(monkey[3][25:])
        if_false = int(monkey[4][25:])

        MAX_VAL *= div_by

        M = Monkey(items, operation[0], operation[1], div_by, if_true, if_false)
        monkeys.append(M)
    return MAX_VAL


MAX_VAL = parse_monkeys()


# part one

# ROUNDS = 20
# for _ in range(ROUNDS):
#     for i, monkey in enumerate(monkeys):
#         for item in monkey.items.copy():
#             worry_level = item
#             amount = item if monkey.op_amount == "old" else int(monkey.op_amount)
#             worry_level = (
#                 worry_level * amount if monkey.operator == "*" else worry_level + amount
#             )
#             worry_level /= 3
#             worry_level = int(worry_level)
#             monkey.items.remove(item)
#             inspect_count[i] += 1

#             if worry_level % monkey.div_by == 0:
#                 monkeys[monkey.true].items.append(worry_level)
#             else:
#                 monkeys[monkey.false].items.append(worry_level)

highest_two = list(sorted(inspect_count, reverse=True))[:2]
# solution_one = highest_two[0] * highest_two[1]

# part two

ROUNDS = 10_000

for _ in range(ROUNDS):
    for i, monkey in enumerate(monkeys):
        for item in monkey.items.copy():
            worry_level = item
            amount = item if monkey.op_amount == "old" else int(monkey.op_amount)
            worry_level = (
                worry_level * amount if monkey.operator == "*" else worry_level + amount
            )
            worry_level = int(worry_level)

            # normalize worry value
            worry_level %= MAX_VAL

            monkey.items.remove(item)
            inspect_count[i] += 1

            if worry_level % monkey.div_by == 0:
                monkeys[monkey.true].items.append(worry_level)
            else:
                monkeys[monkey.false].items.append(worry_level)

highest_two = list(sorted(inspect_count, reverse=True))[:2]
solution_two = highest_two[0] * highest_two[1]


# Automated Submission
if solution_one != EMPTY:
    submit(solution_one, part="a")
if solution_two != EMPTY:
    submit(solution_two, part="b")

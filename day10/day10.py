from aocd import submit, data

EMPTY = object()
solution_one, solution_two = [EMPTY, EMPTY]
# grab data (Cached)
puzzle_data = data
# puzzle_data = """
# addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop
# """.strip()
# -- code below --

out = []


def check_print(cycle, register):
    draw_crt(cycle, register)
    if cycle in [20, 60, 100, 140, 180, 220]:
        out.append(cycle * register)


sprite = [0, 1, 2]
drawn = [["."] * 40 for _ in range(6)]


def draw_crt(cycle, register):
    sprite = [register - 1, register, register + 1]
    if (cycle - 1) % 40 in sprite:
        print(cycle, cycle % 40 - 1, register)
        drawn[cycle // 40][cycle % 40 - 1] = "X"


cycle = 0
register = 1
for i, line in enumerate(puzzle_data.splitlines()):
    instruction = line.split()
    cycle += 1
    if instruction[0] == "noop":
        check_print(cycle, register)
    elif instruction[0] == "addx":
        check_print(cycle, register)
        cycle += 1
        check_print(cycle, register)
        register += int(instruction[1])

# solution_one = sum(out)
for row in drawn:
    for i in row:
        print(i, end="")
    print()

# Automated Submission
if solution_one != EMPTY:
    submit(solution_one, part="a")
if solution_two != EMPTY:
    submit(solution_two, part="b")

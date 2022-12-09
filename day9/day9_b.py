from aocd import submit, data

EMPTY = object()
solution_one, solution_two = [EMPTY, EMPTY]
# grab data (Cached)s
puzzle_data = data

# sample data
# puzzle_data = """
# R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20
# """.strip()
# -- code below --
instructions = [i.split() for i in puzzle_data.splitlines()]
instructions = list(map(lambda x: (x[0], int(x[1])), instructions))


# Coords (bottom-left = 0,0)
knots = []
for _ in range(10):
    knots.append([0, 0])
DIRECTIONS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
VISITED = set()


def sign(x):
    if x == 0:
        return 0
    return x // abs(x)


for letter, count in instructions:
    delta_x, delta_y = DIRECTIONS[letter]
    for i in range(count):
        # add our head movement
        knots[0][0] += delta_x
        knots[0][1] += delta_y
        for tail_i in range(1, len(knots)):
            head_x = knots[tail_i - 1][0]
            head_y = knots[tail_i - 1][1]
            tail_x = knots[tail_i][0]
            tail_y = knots[tail_i][1]
            # case: 2 in any direction
            if head_x == tail_x:
                if abs(head_y - tail_y) >= 2:
                    if tail_y > head_y:
                        tail_y -= 1
                    else:
                        tail_y += 1
            elif head_y == tail_y:
                if abs(head_x - tail_x) >= 2:
                    if tail_x > head_x:
                        tail_x -= 1
                    else:
                        tail_x += 1
            # case: diagonal
            elif abs(head_x - tail_x) >= 2 or abs(head_y - tail_y) >= 2:
                tail_x += sign(head_x - tail_x)
                tail_y += sign(head_y - tail_y)
            # set our tail to our movements
            knots[tail_i][0] = tail_x
            knots[tail_i][1] = tail_y
        VISITED.add((knots[-1][0], knots[-1][1]))


solution_two = len(VISITED)

# Automated Submission
if solution_one != EMPTY:
    submit(solution_one, part="a")
if solution_two != EMPTY:
    submit(solution_two, part="b")

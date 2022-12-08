from aocd import submit, data

EMPTY = object()
solution_one, solution_two = [EMPTY, EMPTY]
# grab data (Cached)
puzzle_data = data
# puzzle_data = """
# 30373
# 25512
# 65332
# 33549
# 35390
# """.strip()
# -- code below --

rows_trees = [list(map(int, tree)) for tree in puzzle_data.splitlines()]

visible = 0

X_SIZE = len(rows_trees[0])
Y_SIZE = len(rows_trees)

# part one

# go through interior
for y, row in enumerate(rows_trees):
    for x, tree in enumerate(row):
        found = [0, 0, 0, 0]
        # check left (from border to x)
        if any(i >= tree for i in row[:x]):
            found[0] = 1
        # check right (from x+1 to border)
        if any(i >= tree for i in row[x + 1 :]):
            found[1] = 1
        # check up (from 0 to y in rows)
        for i in range(0, y):
            if rows_trees[i][x] >= tree:
                found[2] = 1
                break
        # check down (from y+1 to border)
        for i in range(y + 1, Y_SIZE):
            if rows_trees[i][x] >= tree:
                found[3] = 1
                break
        is_visible = any(v == 0 for v in found)
        visible += is_visible


print(f"(1) {visible}")


# part two

max_score = 0

for y, row in enumerate(rows_trees):
    for x, tree in enumerate(row):
        score = [0, 0, 0, 0]
        # find number of indexes until tree

        # left
        for i in range(x - 1, -1, -1):
            score[0] += 1
            if row[i] >= tree:
                break
        # right [x -> X_SIZE]
        for i in range(x + 1, X_SIZE):
            score[1] += 1
            if row[i] >= tree:
                break
        # up
        for i in range(y - 1, -1, -1):
            score[2] += 1
            if rows_trees[i][x] >= tree:
                break

        # down
        for i in range(y + 1, Y_SIZE):
            score[3] += 1
            if rows_trees[i][x] >= tree:
                break
        if x == 2 and y == 3:
            print(score, x, y)
        score = score[0] * score[1] * score[2] * score[3]
        max_score = max(max_score, score)

print(f"(2) {max_score}")

solution_one = visible
solution_two = max_score

# Automated Submission
if solution_one != EMPTY:
    submit(solution_one, part="a")
if solution_two != EMPTY:
    submit(solution_two, part="b")

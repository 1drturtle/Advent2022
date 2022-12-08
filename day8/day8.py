from aocd import submit, data

EMPTY = object()
solution_one, solution_two = [EMPTY, EMPTY]
# grab data (Cached)
puzzle_data = data
# -- code below --

# Automated Submission
if solution_one != EMPTY:
    submit(solution_one, part="a")
if solution_two != EMPTY:
    submit(solution_two, part="a")

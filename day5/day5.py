# input template
from typing import List
from copy import deepcopy


def double_split(content: str):
    return [x.splitlines() for x in content.split("\n\n")]


with open("day5/input.txt") as f:
    file_content = f.read()
#### Code ####
import re

raw_tower, raw_instructions = double_split(file_content)

# build tower
tower_numbers = list(map(int, raw_tower[-1].split()))
tower = [list() for _ in range(tower_numbers[-1])]

for i, row in enumerate(raw_tower[:-1]):
    items = [
        re.sub(r"[\[\],]", "", row[i : i + 4]).strip() for i in range(0, len(row), 4)
    ]
    for i, item in enumerate(items):
        if item != "":
            tower[i].append(item)
tower = [x[::-1] for x in tower]
tower_2 = deepcopy(tower)

# instructions
for raw_instr in raw_instructions:
    _, count, _, from_col, _, to_col = raw_instr.split(" ")
    from_col = int(from_col) - 1
    to_col = int(to_col) - 1
    # part one code
    for _ in range(int(count)):
        tower[to_col].append(tower[from_col].pop())

    to_move = []

    # part two code
    for _ in range(int(count)):
        to_move.append(tower_2[from_col].pop())
    to_move = to_move[::-1]
    tower_2[to_col] += to_move

out = "".join(x[-1] for x in tower if x)
out_2 = "".join(x[-1] for x in tower_2 if x)
#### output ####
print(f"(1) {out}")
print(f"(2) {out_2}")

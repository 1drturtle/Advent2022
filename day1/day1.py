# get input
with open("day1/input.txt") as f:
    file_content = f.read()

# parse into total calorie count
elves = sorted(
    map(sum, [map(int, elf.splitlines()) for elf in file_content.split("\n\n")]),
    reverse=True,
)

# part one
print(f"Part 1: Highest # of Calories = {elves[0]}")
# part two
print(f"Part 2: Sum of top three = {sum(elves[0:3])}")

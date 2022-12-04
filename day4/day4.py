# input template
with open("day4/input.txt") as f:
    file_content = f.read()
#### Code ####

# variables
pairs = file_content.splitlines()
pair_count = 0
disjoint_count = 0


def dash_to_range(x: str):
    x = x.split("-")
    return set(range(int(x[0]), int(x[-1]) + 1))


for pair in pairs:
    left, right = (dash_to_range(side) for side in pair.split(","))
    # part one
    if left.issubset(right) or right.issubset(left):
        pair_count += 1
    # part two
    if (not left.isdisjoint(right)) or (not right.isdisjoint(left)):
        disjoint_count += 1

#### output ####
print(f"(1) {pair_count}")
print(f"(1) {disjoint_count}")

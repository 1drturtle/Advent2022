# input template
with open("day3/input.txt") as f:
    file_content = f.read()
#### Code ####

# use letters to get index and point array to use index
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
points = list(range(1, len(letters) + 1))
# each sack is on a new line
sacks = file_content.splitlines()
# part one
prio_total = sum(
    sum(
        points[letters.index(c)]
        for c in set(sack[: len(sack) // 2])
        if c in sack[len(sack) // 2 :]
    )
    for sack in sacks
)

# part two

# each group is 3 sacks, so make lists of the next 3 sacks
groups = [sacks[i : i + 3] for i in range(0, len(sacks), 3)]
badge_total = sum(
    sum(
        points[letters.index(c)]
        for c in set(group[0])
        if c in group[1] and c in group[2]
    )
    for group in groups
)


#### output ####
print(f"(1) {prio_total}")
print(f"(2) {badge_total}")

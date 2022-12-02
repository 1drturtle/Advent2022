# input template
with open("day2/input.txt") as f:
    file_content = f.read().splitlines()
#### Code ####
point_val = {"X": 1, "Y": 2, "Z": 3}
p_win = {"A": 2, "B": 3, "C": 1}
p_lose = {"A": 3, "B": 1, "C": 2}
p_draw = {"A": 1, "B": 2, "C": 3}
total_score = 0
total_score_two = 0


# X = lose
# Y = draw
# Z = win
# rock -> paper
# paper -> scissors
# scissors -> rock

for line in file_content:
    first, second = line.split()
    # part one
    total_score += point_val[second]
    match second:
        case "X":
            total_score += 6 if first == "C" else 3 if first == "A" else 0
        case "Y":
            total_score += 6 if first == "A" else 3 if first == "B" else 0
        case "Z":
            total_score += 6 if first == "B" else 3 if first == "C" else 0
    # part two
    match second:
        case "X":
            total_score_two += 0 + p_lose[first]
        case "Y":
            total_score_two += 3 + p_draw[first]
        case "Z":
            total_score_two += 6 + p_win[first]

#### output ####
print(f"(1) total score: {total_score}")
print(f"(2) total score two: {total_score_two}")

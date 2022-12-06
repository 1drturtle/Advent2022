# input template
with open("day6/input.txt") as f:
    file_content = f.read()
#### Code ####


def check_next_x(content: str, x: int):
    for i in range(len(file_content)):
        words = file_content[i : i + x]
        unique = set(words)
        if len(unique) == x:
            break

    return i + x


# part one
print(f"(1) {check_next_x(file_content, 4)}")

# part two
print(f"(2) {check_next_x(file_content, 14)}")
#### output ####

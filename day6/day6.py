# input template
with open("day6/input.txt") as f:
    file_content = f.read()
#### Code ####

# part one
buffer = ""
for i in range(len(file_content)):
    words = file_content[i : i + 4]
    unique = set(words)
    if len(unique) == 4:
        break

print(f"(1) {i + 4}")

# part two
buffer = ""
for i in range(len(file_content)):
    words = file_content[i : i + 14]
    unique = set(words)
    if len(unique) == 14:
        break
print(f"(2) {i + 14}")
#### output ####

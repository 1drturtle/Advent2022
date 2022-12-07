# input template
with open("day7/input.txt") as f:
    file_content = f.read()
#### Code ####

directories = {}
split_by_command = [x.strip().splitlines() for x in file_content.split("$")][2:]
current_dir = "/"

# split lines by commands
for item in split_by_command:
    command = item[:1][0].split()
    output = item[1:]
    dir_list = current_dir.split("/")[1:-1]

    current_dictionary = directories
    for dir_name in dir_list:
        current_dictionary = current_dictionary[dir_name]

    if command[0] == "ls":
        for o in output:
            o = o.split()
            if o[0].startswith("dir"):
                current_dictionary[o[1]] = current_dictionary.get(o[1], {})
            else:
                current_dictionary[o[1]] = int(o[0])
    elif command[0] == "cd":
        if command[1] == "/":
            current_dir = "/"
        elif command[1] != "..":
            current_dir += command[1] + "/"
        elif command[1] == "..":
            current_dir = "/" + "".join(f"{x}/" for x in dir_list[:-1])


def get_dir_size(directory: dict):
    total = 0
    for k, v in directory.items():
        if type(v) == dict:
            total += get_dir_size(v)
        else:
            total += v
    return total


def get_all_dirs(dir):
    dirs = [dir]
    for _, v in dir.items():
        if type(v) == dict:
            dirs += get_all_dirs(v)
    return dirs


# part one

dir_total = sum(
    get_dir_size(x) for x in get_all_dirs(directories) if get_dir_size(x) <= 100_000
)

# part two

TOTAL_DISK_SIZE = 70_000_000
CURRENT_UNUSED = TOTAL_DISK_SIZE - get_dir_size(directories)
NEEDED = 30000000

smallest_to_biggest = sorted(get_dir_size(x) for x in get_all_dirs(directories))

ours = [x for x in smallest_to_biggest if (CURRENT_UNUSED + x) >= NEEDED][0]

#### output ####
print(f"(1) {dir_total}")
print(f"(2) {ours}")

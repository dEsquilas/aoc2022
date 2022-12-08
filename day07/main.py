import pytest

def day_7(filename):

    lines = [l.strip() for l in open(filename).readlines()]

    directories_size = {}
    path = []

    for i in range(len(lines)):
        current_line = lines[i]
        if current_line == "$ cd ..":
            path.pop()
        elif "$ cd " in current_line:
            path.append(current_line.split()[-1])
        if current_line == "$ ls":
            directories_size["/".join(path)] = 0
            i += 1
            while i < len(lines) and not "$ cd" in lines[i]:
                if not "dir" in lines[i]:
                    file_size= lines[i].split(" ")[0]
                    for j in range (1, len(path) + 1):
                        directories_size["/".join(path[:j])] += int(file_size)
                i += 1

    output_p1 = 0

    free_space = 30000000 - (70000000 - directories_size["/"])
    bigger_directories = []

    for directory in directories_size:
        if directories_size[directory] <= 100000:
            output_p1 += directories_size[directory]
        if free_space < directories_size[directory]:
            bigger_directories.append(directories_size[directory])

    bigger_directories.sort()
    output_p2 = bigger_directories[0]

    return output_p1, output_p2


def test_day_7():
    assert day_7("test.txt") == (95437, 24933642)


test_day_7()

p1, p2 = day_7("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

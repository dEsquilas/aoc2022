import pytest

def calculate_directory_size(path, directories, files_in_directories, directories_bigger = [], free_space = False):
    size = 0
    for file in files_in_directories[path]:
        size += int(file[1])
    for dir in directories[path]:
        size += calculate_directory_size(path + "/" + dir, directories, files_in_directories, directories_bigger)

    if free_space and size > free_space:
        directories_bigger.append(size)

    return size


def day_7(filename):

    lines = [l.strip() for l in open(filename).readlines()]

    directories = {}
    files_in_directories = {}
    path = []

    for i in range(len(lines)):
        current_line = lines[i]
        if current_line == "$ cd ..":
            path.pop()
        elif "$ cd " in current_line:
            path.append(current_line.split()[-1])
        if current_line == "$ ls":
            current_directory = lines[i-1].split(" ")[-1]
            directories["/".join(path)] = []
            files_in_directories["/".join(path)] = []
            i += 1
            while i < len(lines) and not "$ cd" in lines[i]:
                if "dir" in lines[i]:
                    dir = lines[i].split(" ")[-1]
                    directories["/".join(path)].append(dir)
                else:
                    file_size, file_name = lines[i].split(" ")
                    files_in_directories["/".join(path)].append((file_name, file_size))
                i += 1

    output_p1 = 0

    root_size = calculate_directory_size("/", directories, files_in_directories)
    total_size = 70000000
    needed_size = 30000000
    free_space_needed = needed_size - (total_size - root_size)

    directories_bigger = []

    for directory in directories:
        current_size = calculate_directory_size(directory, directories, files_in_directories, directories_bigger, free_space_needed)
        if current_size <= 100000:
            output_p1 += current_size

    directories_bigger.sort()
    output_p2 = directories_bigger[0]

    return output_p1, output_p2


def test_day_7():
    assert day_7("test.txt") == (95437, 24933642)


test_day_7()


p1, p2 = day_7("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

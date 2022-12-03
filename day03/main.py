import pytest

def day_3(filename):
    lines = [l.strip() for l in open(filename)]

    total_p1 = 0
    total_p2 = 0

    # Part 1
    for line in lines:

        item = next(iter(set(line[:len(line) // 2]) & set(line[len(line) // 2:])))
        if item.isupper():
            total_p1 += ord(item) - ord('A') + 27
        else:
            total_p1 += ord(item) - ord('a') + 1

    # Part 2
    for i in range(len(lines)//3):
        item = next(iter(set(lines[i*3]) & set(lines[i*3+1]) & set(lines[i*3+2])))
        if item.isupper():
            total_p2 += ord(item) - ord('A') + 27
        else:
            total_p2 += ord(item) - ord('a') + 1

    return total_p1, total_p2

def test_day_3():
     assert day_3("test.txt") == (157, 70)


test_day_3()

p1, p2 = day_3("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)

import pytest

def day_1(filename):
    lines = [l.strip() for l in open(filename)]

    current_total = 0
    current_results = []

    for line in lines:
        if line == "":
            current_results.append(current_total)
            current_total = 0
            continue
        else:
            current_total += int(line)

    current_results.append(current_total)
    current_results.sort(reverse=True)

    return current_results[0], current_results[0] + current_results[1] + current_results[2]


def test_day_1():
     assert day_1("test.txt") == (24000, 45000)


test_day_1()

p1, p2 = day_1("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)

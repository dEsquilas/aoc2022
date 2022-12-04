import pytest

def day_4(filename):
    lines = [l.strip() for l in open(filename)]
    total_p1, total_p2 = 0, 0

    for line in lines:
        pair1, pair2 = line.split(",")
        p1r1, p1r2 = pair1.split("-")
        p2r1, p2r2 = pair2.split("-")

        p1r1, p1r2 = int(p1r1), int(p1r2)
        p2r1, p2r2 = int(p2r1), int(p2r2)

        if (p1r1 <= p2r1 and p1r2 >= p2r2) or (p2r1 <= p1r1 and p2r2 >= p1r2):
            total_p1 += 1



    return total_p1, total_p2


def test_day_4():
     assert day_4("test.txt") == (2, 4)

test_day_4()

p1, p2 = day_4("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)
import pytest

def is_bigger(axis, offset):
    return is_biggger_subpart(axis[:offset], axis[offset]) or is_biggger_subpart(axis[offset + 1:], axis[offset])

def is_biggger_subpart(part, value):
    part.sort()
    part.reverse()
    if part[0] < value and part.count(value) == 0:
        return True
    else:
        return False

def get_score(axis, offset):

    left = axis[:offset]
    left.reverse()
    right = axis[offset + 1:]

    score_p1 = get_subscore(left, axis[offset])
    score_p2 = get_subscore(right, axis[offset])

    return score_p1 * score_p2


def get_subscore(axis, value):
    for i in range(len(axis)):
        if axis[i] >= value:
            return i+1
    return i+1

def day_8(filename):

    map = [l.strip() for l in open(filename).readlines()]

    visibles = 0
    max_score = 0

    for line, row in enumerate(map):
        for col, item in enumerate(row):
            if line == 0 or line == len(map) - 1 or col == 0 or col == len(row) - 1:
                visibles += 1
            else:
                x_axis = [int(map[line][i]) for i in range(len(map))]
                y_axis = [int(map[i][col]) for i in range(len(map))]
                if is_bigger(x_axis, col) or is_bigger(y_axis, line):
                    visibles += 1
                score = get_score(x_axis, col) * get_score(y_axis, line)
                max_score = max(max_score, score)

    output_p1 = visibles
    output_p2 = max_score

    return output_p1, output_p2


def test_day_8():
    assert day_8("test.txt") == (21, 8)

test_day_8()

p1, p2 = day_8("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

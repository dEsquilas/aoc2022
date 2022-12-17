import pytest
from pprint import pprint

hslash = [
    [0, 0, 1, 1, 1, 1, 0]
]
cross = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
]
vslash = [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0]
]
square = [
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0]
]

def apply_to_map(map, direction):

    if direction == 1:
        for row in map:
            for i in len(row) - 1:
                if i == 0:
                    row[i] = 0
                    row[i+1] = row[i]
                else:



def day_17(filename):

    floor_width = 7
    current_floor_level = 0
    start_left = 2
    start_top = 3

    l = open(filename).readline()


    figures = [hslash, cross, vslash, square]
    current_figure = 0

    map = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    current_map = hslash + map

    pprint(current_map)


    return 0, 0


def test_day_17():
    assert day_17("test.txt") == (0, 0)


test_day_17()
exit()
p1, p2 = day_17("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

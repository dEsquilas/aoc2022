import copy

import pytest
from pprint import pprint

def has_common_faces(cube1, cube2):
    if (cube1[0] == cube2[0] and cube1[1] == cube2[1] and abs(cube1[2] - cube2[2]) == 1) or \
        (cube1[1] == cube2[1] and cube1[2] == cube2[2] and abs(cube1[0] - cube2[0]) == 1) or \
        (cube1[2] == cube2[2] and cube1[0] == cube2[0] and abs(cube1[1] - cube2[1]) == 1):
        return True
    return False


def day_18(filename):

    lines = [l for l in open(filename).read().splitlines()]
    faces = set()
    current_faces = 0
    cubes_added = set()

    for line in lines:
        t = [int(x) for x in line.split(",")]
        faces.add((int(t[0]), int(t[1]), int(t[2])))

    while(len(faces) > 0):
        if len(cubes_added) == 0:
            cubes_added.add(faces.pop())
            current_faces = 6
        else:
            faces_to_add = 6
            current_cube = faces.pop()
            for cube in cubes_added:
                if has_common_faces(cube, current_cube):
                    faces_to_add -= 2
            cubes_added.add(current_cube)
            current_faces += faces_to_add

    # flood from 0, 0, 0 to limit the number

    external_air_blocks = set()
    border_to_expand = set()
    directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

    faces = 0

    external_air_blocks.add((-1, -1, -1))
    border_to_expand.add((-1, -1, -1))

    limit_min = -1
    limit_max = 0

    for c in cubes_added:
        b = max(c)
        if b > limit_max:
            limit_max = b

    limit_max += 1

    while border_to_expand:
        current_cube = border_to_expand.pop()
        for direction in directions:
            new_cube = (current_cube[0] + direction[0], current_cube[1] + direction[1], current_cube[2] + direction[2])

            if new_cube[0] < limit_min or new_cube[1] < limit_min or new_cube[2] < limit_min:
                continue
            if new_cube[0] > limit_max or new_cube[1] > limit_max or new_cube[2] > limit_max:
                continue

            if new_cube in cubes_added:
                faces += 1

            if new_cube not in external_air_blocks and new_cube not in cubes_added:
                external_air_blocks.add(new_cube)
                border_to_expand.add(new_cube)

    return current_faces, faces


def test_day_18():
    assert day_18("test.txt") == (64, 58)


test_day_18()
p1, p2 = day_18("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

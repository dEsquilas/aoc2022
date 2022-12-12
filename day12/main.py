import pytest
import astar


def day_12(filename):


    dir = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    lines = [l.strip() for l in open(filename).read().split("\n")]
    int_map = []

    for line in lines:
        int_map.append([ord(i) for i in list(line)])

    map = {}

    # 83 S
    # 69 E

    for y in range(len(int_map)):
        for x in range(len(int_map[0])):
            if int_map[y][x] == 83:
                int_map[y][x] = 96
            if int_map[y][x] == 69:
                int_map[y][x] = 123

    for y in range(len(int_map)):
        for x in range(len(int_map[0])):

            current = int_map[y][x]
            map[(y, x)] = []

            if current == 123:
                end = (y, x)
            if current == 96:
                start = (y, x)

            for (dx, dy) in dir:
                cx = x + dx
                cy = y + dy

                if 0 <= cy < len(int_map) and 0 <= cx < len(int_map[0]) and (int_map[cy][cx] <= current + 1):
                    map[(y, x)].append((cy, cx))

    def neighbors(n):
        for n1 in map[n]:
            yield n1

    path_p1 = list(astar.find_path(start, end, neighbors_fnct=neighbors, heuristic_cost_estimate_fnct=lambda x,y: 1))

    paths = []

    for y in range(len(int_map)):
        for x in range(len(int_map[0])):
            if int_map[y][x] == 97:
                path = astar.find_path((y, x), end, neighbors_fnct=neighbors,
                                heuristic_cost_estimate_fnct=lambda x,y: 1)

                if path != None:
                    paths.append(len(list(path)) -1)

    return len(path_p1) - 1, sorted(paths)[0]


def test_day_12():
    assert day_12("test.txt") == (31, 29)


test_day_12()
p1, p2 = day_12("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

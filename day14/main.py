import pytest


def day_14(filename):

    rocks_input = [l.strip() for l in open(filename).readlines()]
    rocks = set()
    bottom_limit = 0
    cycle = 0
    cycle_p1 = 0

    for rock in rocks_input:
        rock_part = [tuple(map(int, p.split(","))) for p in rock.split(" -> ")]
        for i in range(len(rock_part)):

            if rock_part[i][1] > bottom_limit:
                bottom_limit = rock_part[i][1]

            if i > 0:

                from_x = last_x
                to_x = rock_part[i][0] + 1
                from_y = last_y
                to_y = rock_part[i][1] + 1

                if last_x - rock_part[i][0] > 0:
                    from_x = rock_part[i][0]
                    to_x = last_x + 1

                if last_y - rock_part[i][1] > 0:
                    from_y = rock_part[i][1]
                    to_y = last_y + 1

                for x in range(from_x, to_x):
                    for y in range(from_y, to_y):
                        rocks.add((x, y))
            last_x = rock_part[i][0]
            last_y = rock_part[i][1]


    while True:
        current_sand = (500, 0)
        if current_sand in rocks:
            break
        while True:

            next_available = (current_sand[0], current_sand[1] + 1)

            if cycle_p1 == 0 and current_sand[1] == bottom_limit:
                cycle_p1 = cycle

            if next_available[1] == bottom_limit + 2:
                break
            elif next_available not in rocks:
                pass
            else:
                if (next_available[0] - 1, next_available[1]) not in rocks:
                    next_available = next_available[0] - 1, next_available[1]
                elif (next_available[0] + 1, next_available[1]) not in rocks:
                    next_available = next_available[0] + 1, next_available[1]
                else:
                    break

            current_sand = next_available

        rocks.add(current_sand)
        cycle += 1

    return cycle_p1, cycle


def test_day_14():
    assert day_14("test.txt") == (24, 93)


test_day_14()
p1, p2 = day_14("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

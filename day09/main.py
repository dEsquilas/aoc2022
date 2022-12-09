import pytest


def move(behind_knot, current_knot):
    if abs(behind_knot[0] - current_knot[0]) <= 1 and abs(behind_knot[1] - current_knot[1]) <= 1:
        return current_knot
    elif abs(behind_knot[0] - current_knot[0]) >= 2 and abs(behind_knot[1] - current_knot[1]) >= 2:
        if behind_knot[0] > current_knot[0]:
            x_coord = behind_knot[0] - 1
        else:
            x_coord = behind_knot[0] + 1

        if behind_knot[1] > current_knot[1]:
            y_coord = behind_knot[1] - 1
        else:
            y_coord = behind_knot[1] + 1

        return x_coord, y_coord
    elif abs(behind_knot[0] - current_knot[0]) >= 2:
        if behind_knot[0] > current_knot[0]:
            x_coord = behind_knot[0] - 1
        else:
            x_coord = behind_knot[0] + 1
        return x_coord, behind_knot[1]
    elif abs(behind_knot[1] - current_knot[1]) >= 2:
        if behind_knot[1] > current_knot[1]:
            y_coord = behind_knot[1] - 1
        else:
            y_coord = behind_knot[1] + 1
        return behind_knot[0], y_coord


def calculate_by_knots(orders, knots):
    x_head, y_head = 0, 0
    knots_position = [(0, 0) for i in range(knots)]
    positions_visited_0 = {}
    positions_visited_last = {}

    for order in orders:
        movement, distance = order.split(" ")
        for i in range(int(distance)):
            if movement == "U":
                y_head += 1
            elif movement == "D":
                y_head -= 1
            elif movement == "R":
                x_head += 1
            elif movement == "L":
                x_head -= 1

            for j in range(0, knots):
                if j == 0:
                    knots_position[j] = move((x_head, y_head), knots_position[j])
                else:
                    knots_position[j] = move(knots_position[j-1], knots_position[j])

            positions_visited_0[knots_position[0]] = True
            positions_visited_last[knots_position[len(knots_position)-1]] = True

    return len(positions_visited_0), len(positions_visited_last)


def day_9(filename):

    orders = [l.strip() for l in open(filename).readlines()]
    output_p1, output_p2 = calculate_by_knots(orders, 9)

    return output_p1, output_p2


def test_day_9():
    assert day_9("test.txt") == (13, 1)
    assert day_9("test2.txt") == (88, 36)


test_day_9()

p1, p2 = day_9("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

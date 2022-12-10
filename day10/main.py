import pytest


def day_10(filename):

    orders = [l.strip() for l in open(filename).readlines()]
    stack = [0]
    signal = 0

    for order in orders:
        if "noop" in order:
            stack.append(0)
        else:
            cmd = order.split(" ")
            stack.append(0)
            stack.append(int(cmd[1]))

    x = 1
    screen = [" " for i in range(40)]

    for i in range(1, len(stack)):

        tmp = stack.pop(0)
        x += tmp

        pixel_position = (i - 1) % 40

        if abs(x - pixel_position) <= 1:
            screen[pixel_position] = '#'


        if i == 20 or (i >= 20 and (i - 20) % 40 == 0):
            current = i * x
            signal += current

        if i % 40 == 0:
            print(''.join(screen))
            screen = [" " for i in range(40)]

        i += 1


    return signal, 0


def test_day_10():
    assert day_10("test.txt") == (13140, 0)

test_day_10()

print(" ")
p1, p2 = day_10("input.txt")

print(" ")
print("Part 1:", p1)


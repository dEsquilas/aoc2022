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
    screen = []
    line_screen = ["." for i in range(40)]

    for i in range(1, len(stack)):

        x += stack.pop(0)
        pixel_position = (i - 1) % 40

        if -1 <= x - pixel_position <= 1:
            line_screen[pixel_position] = '#'

        if i == 20 or (i >= 20 and (i - 20) % 40 == 0):
            current = i * x
            signal += current

        i += 1

        if i % 40 == 0:
            screen.append(line_screen)
            line_screen = ["." for i in range(40)]

    p2 = []
    for line_screen in screen:
        p2.append("".join(line_screen))

    return signal, p2


def test_day_10():
    assert day_10("test.txt")[0] == 13140

test_day_10()

p1, p2 = day_10("input.txt")

print("Part 1:", p1)
print("Part 2:")
for line in p2:
    print(line)


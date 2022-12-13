import functools

import pytest
from pprint import pprint

def compare(a, b):

    type_a = type(a)
    type_b = type(b)

    # ints

    if type_a == int and type_b == int and a < b:
        return 1
    elif type_a == int and type_b == int and a == b:
        return 0
    elif type_a == int and type_b == int and a > b:
        return -1


    # ints - list

    if type_a is list and type_b is int:
        return compare(a, [b])
    if type_a is int and type_b is list:
        return compare([a], b)

    # lists

    if type_a is list and type_b is list:
        for i in range(len(a)):
            if i > len(b) - 1:
                return -1
            ret = compare(a[i], b[i])
            if ret != 0:
                return ret

        if len(a) == len(b):
            return 0
        if len(b) > len(a):
            return 1

    return -1


def day_13(filename):

    packets_input = [l.strip() for l in open(filename).read().split("\n\n")]
    packets = []
    output_p1 = 0
    output_p2 = 1

    for i in range(len(packets_input)):

        a, b = packets_input[i].split("\n")

        a = eval(a)
        b = eval(b)

        ret = compare(a, b)

        packets.append(a)
        packets.append(b)

        if ret == 1:
            output_p1 += i + 1

    packets.append([[2]])
    packets.append([[6]])

    packets = sorted(packets, key=functools.cmp_to_key(lambda a,b: compare(a,b)), reverse=True)

    for i in range(len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            output_p2 *= (i+1)

    return output_p1, output_p2


def test_day_13():
    assert day_13("test.txt") == (13, 140)

test_day_13()
p1, p2 = day_13("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

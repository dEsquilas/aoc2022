import pytest
import copy
from parse import parse


def day_5(filename):
    lines = [l for l in open(filename)]

    first_line = True
    stacks = []

    start_on = 0
    output_p1 = ""
    output_p2 = ""

    for i in range(len(lines[0]) // 4):
        stacks.append([])

    for id, line in enumerate(lines):
        i = 0
        current_block = 0
        while i < len(line):
            block = line[i:i+3]
            if block != "   ":
                stacks[current_block].append(block[1:2])
            current_block += 1
            i+=4
        if lines[id+2].strip() == "":
            start_on = id + 3
            break

    stacks_p1 = copy.deepcopy(stacks)
    stacks_p2 = copy.deepcopy(stacks)

    for i in range(len(stacks)):
        stacks_p1[i].reverse()

    for i in range(start_on, len(lines)):
        count, from_item, to_item = parse("move {} from {} to {}", lines[i].strip())
        for j in range(int(count)):
            stacks_p1[int(to_item)-1].append(stacks_p1[int(from_item)-1].pop())


    for i in range(len(stacks_p1)):
        output_p1 += stacks_p1[i].pop()

    for i in range(len(stacks)):
        stacks_p2[i].reverse()


    for i in range(start_on, len(lines)):
        count, from_item, to_item = parse("move {} from {} to {}", lines[i].strip())
        pos_to_pop = len(stacks_p2[int(from_item) - 1]) - int(count)
        for j in range(int(count)):
            item = stacks_p2[int(from_item) - 1].pop(pos_to_pop)
            stacks_p2[int(to_item)-1].append(item)

    for i in range(len(stacks_p1)):
        output_p2 += stacks_p2[i].pop()


    return output_p1, output_p2


def test_day_5():
     assert day_5("test.txt") == ("CMZ", "MCD")

test_day_5()

p1, p2 = day_5("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)
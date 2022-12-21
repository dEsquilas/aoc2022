import pytest
import copy
from pprint import pprint

def find_position(value, numbers):
    for i in range(len(numbers)):
        if numbers[i][0] == value and numbers[i][1] == False:
            return i

def p(numbers):
    for n in numbers:
        print(n[0], end=" ")
    print()


def day_20(filename):

    numbers = [(int(l), False, id) for (id, l) in enumerate(open(filename).read().splitlines())]
    numbers_original = copy.deepcopy(numbers)

    p(numbers)

    expected = [
        "2 1 -3 3 -2 0 4",
        "1 -3 2 3 -2 0 4",
        "1 2 3 -2 -3 0 4",
        "1 2 -2 -3 0 3 4",
        "1 2 -3 0 3 4 -2",
        "1 2 -3 0 3 4 -2",
        "1 2 -3 4 0 3 -2"
    ]

    for current_position in range(len(numbers_original)):
        current_number = numbers_original[current_position][0]


        pos = find_position(current_number, numbers)
        pos_to_insert = pos + current_number

        numbers.pop(pos)

        while pos_to_insert >= len(numbers):
            pos_to_insert -= len(numbers)

        while pos_to_insert < 0:
             pos_to_insert += len(numbers)

        # if pos_to_insert < pos:
        #     pos_to_insert += 1

        if pos_to_insert == 0:
            pos_to_insert = len(numbers)


        #print("\nInserting ", current_number, " at ", pos_to_insert, "from", pos)

        recreated_numbers = []
        i = 0
        while numbers:
            if i == pos_to_insert:
                recreated_numbers.append((current_number, True))
                i += 1
            recreated_numbers.append(numbers.pop(0))
            i += 1
            if i == pos_to_insert:
                recreated_numbers.append((current_number, True))
                i += 1

        numbers = recreated_numbers
        #print(expected[current_position], " - Expected")
        #p(numbers)


    offset = -1

    for i in range(len(numbers)):
        if offset == -1 and numbers[i][0] == 0:
            offset = i
            break

    p1 = numbers[(1000 + offset) % len(numbers)][0] + numbers[(2000 + offset) % len(numbers)][0] + numbers[(3000 + offset) % len(numbers)][0]

    return p1, 0


def test_day_20():
    assert day_20("test.txt") == (3, 0)


test_day_20()
exit()
p1, p2 = day_20("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

#import pytest
import copy
from pprint import pprint

def find_position(value, numbers, iter):
    for i in range(len(numbers)):
        if iter > 1:
            if numbers[i][0] * 811589153 == value and numbers[i][1] == False:
                return i
        else:
            if numbers[i][0] == value and numbers[i][1] == False:
                return i


def check_all_keys_exists(numbers):

    for i in range(len(numbers)):
        found = False
        for j in range(len(numbers)):
            if numbers[j][2] == i:
                found = True
                break
        if not found:
            print("Not found", i, " kkkk")
            return False

    return True



def solve(numbers, iter):

    for x in range(iter):

        for n in range(len(numbers)):
            numbers[n] = (numbers[n][0], False, numbers[n][2])

        if x > 0:
            pprint(numbers)
            print(x)

        for position_to_move in range(len(numbers)):
            #print("ptm", position_to_move)
            # Find the next
            current_position = -1

            for i in range(len(numbers)):
                if numbers[i][2] == position_to_move:
                    current_position = i
                    break

            if current_position == -1:
                pprint(numbers)
                print(position_to_move, i, x)
                exit()

            def_value = numbers[current_position][0]

            if iter > 1:
                current_number = numbers[current_position][0] * 811589153
            else:
                current_number = numbers[current_position][0]
            current_id = numbers[current_position][2]


            pos = find_position(current_number, numbers, iter)

            if pos is None:
                print(pos, current_number, numbers, x)

            pos_to_insert = pos + current_number

            numbers.pop(pos)

            if pos_to_insert >= len(numbers):
                pos_to_insert %= len(numbers)

            if pos_to_insert < 0:
                 pos_to_insert %= len(numbers)


            if pos_to_insert == 0:
                pos_to_insert = len(numbers)


            #print("\nInserting ", current_number, " at ", pos_to_insert, "from", pos)

            recreated_numbers = []
            i = 0

            found = False
            while numbers:

                if i == 880:
                    found = True

                if i == pos_to_insert:
                    recreated_numbers.append((def_value, True, current_id))
                    i += 1
                if i == 880:
                    found = True
                recreated_numbers.append(numbers.pop(0))
                i += 1
                if i == 880:
                    found = True
                if i == pos_to_insert:
                    recreated_numbers.append((def_value, True, current_id))
                    i += 1
                if i == 880:
                    found = True

            numbers = recreated_numbers


            if not check_all_keys_exists(numbers):
                print(numbers)
                print("Error")
                exit()


            #print(expected[current_position], " - Expected")
            #p(numbers)
            #pprint(numbers, width=100)


    offset = -1

    for i in range(len(numbers)):
        if offset == -1 and numbers[i][0] == 0:
            offset = i
            break

    p1 = numbers[(1000 + offset) % len(numbers)][0] + numbers[(2000 + offset) % len(numbers)][0] + numbers[(3000 + offset) % len(numbers)][0]
    if iter > 1:
        p1 *= 811589153

    return p1

def day_20(filename):

    # numbers = [(int(l), False, id) for (id, l) in enumerate(open(filename).read().splitlines())]
    #
    # p1 = solve(copy.deepcopy(numbers), 1)

    numbers_2 = [(int(l), False, id) for (id, l) in enumerate(open(filename).read().splitlines())]

    p2 = solve(copy.deepcopy(numbers_2), 10)

    print(p1, p2)

    return p1, p2


def test_day_20():
    assert day_20("test.txt") == (3, 1623178306)


#test_day_20()
p1, p2 = day_20("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

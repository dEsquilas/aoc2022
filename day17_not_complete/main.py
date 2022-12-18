import copy

import pytest
from pprint import pprint

hslash = [
    [0, 0, 1, 1, 1, 1, 0]
]
cross = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
]
reversed_l = [
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
]
vslash = [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0]
]
square = [
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0]
]
zero = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def pmap(map):
    # print the map, print space if 0, print @ if 1, print # if 2
    print("----------------")
    for row in map:
        for i in row:
            if i == 0:
                print(".", end="")
            if i == 1:
                print("@", end="")
            if i == 2:
                print("#", end="")
        print("")



def  can_i_move_side(map, direction):

    if direction == 1:
        pos_to_check = 6
    else:
        pos_to_check = 0
    for row in map:
        if row[pos_to_check] == 1:
            return False

    return True

def move_side(map, direction):

    # check if can I move to the direction
    aux_map = copy.deepcopy(map)

    if direction == 1:
        # the map has 1, 2 or 0
        # move to the right the 1's, dont touch the 2's
        for row_id in range(len(map)):
            for i in reversed(range(len(map[row_id]))):
                if map[row_id][i] == 1:
                    map[row_id][i+1] = 1
                    map[row_id][i] = 0

    if direction == -1:
        # the map has 1, 2 or 0
        # move to the left the 1's, dont touch the 2's
        for row_id in range(len(map)):
            for i in range(len(map[row_id])):
                if map[row_id][i] == 1:
                    map[row_id][i-1] = 1
                    map[row_id][i] = 0






def can_i_move_down(map):

    # check if can move the 1's down on the map
    # can move to down if the next position down is 0
    # if there is a 2 or is the last row, return False
    for row_id in range(len(map)):
        for i in range(len(map[row_id])):
            if map[row_id][i] == 1:
                if row_id == len(map)-1:
                    return False
                if map[row_id+1][i] == 2:
                    return False

    # for id_row in range(len(map)-1):
    #     for i in range(len(map[id_row])):
    #         current_row = id_row
    #         next_row = id_row + 1
    #         if map[current_row][i] == 1 and map[next_row][i] != 0 and map[next_row][i] != 1:
    #             return False
    #
    # for i in map[-1]:
    #     if i == 1:
    #         return False

    return True

def move_down(map):

    # the map has 1, 2 or 0
    # move to down the 1's, dont touch the 2's

    for row_id in reversed(range(len(map))):
        for i in range(len(map[row_id])):
            if map[row_id][i] == 1:
                map[row_id+1][i] = 1
                map[row_id][i] = 0


def fix(map):
    for row_id in range(len(map)):
        for i in range(len(map[row_id])):
            if map[row_id][i] == 1:
                map[row_id][i] = 2

def clean(map):
    # remove all rows that are all 0
    for row_id in reversed(range(len(map))):
        if sum(map[row_id]) == 0:
            map.pop(row_id)


def day_17(filename):

    floor_width = 7
    current_floor_level = 0
    start_left = 2
    start_top = 3

    l = open(filename).readline()
    directions = [1 if c == ">" else -1 for c in l]
    current_direction = 0

    figures = [hslash, cross, reversed_l, vslash, square]
    current_figure = 0

    map = []
    cycle = 0

    while cycle < 2:

        sub_figure = copy.deepcopy(figures[current_figure])
        sub_zero = copy.deepcopy(zero)
        sub_map = copy.deepcopy(map)


        map = sub_figure + sub_zero + sub_map


        while can_i_move_down(map):
            if can_i_move_side(map, directions[current_direction]):
                move_side(map, directions[current_direction])
            current_direction += 1
            if current_direction == len(directions):
                current_direction = 0
            move_down(map)



        fix(map)
        #clean(map)
        pmap(map)
        pprint("---------------- FIXED")

        cycle += 1

        current_figure += 1
        if current_figure >= len(figures):
            current_figure = 0

    return 0, 0


def test_day_17():
    assert day_17("test.txt") == (0, 0)


test_day_17()
exit()
p1, p2 = day_17("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

import pytest


# Part 1
# A - X = Rock
# B - Y = Paper
# C - Z = Scissors

# Part 2
# X - Lose
# Y - Draw
# Z - Win

def day_2(filename):
    lines = [l.strip() for l in open(filename)]

    total_score_p1 = 0
    total_score_p2 = 0

    for line in lines:
        he, me = line.split(" ")

        tmp = me

        he = ord(he)
        me = ord(tmp) - (ord("X") - ord("A"))


        if he == me:
            total_score_p1 += 3
        if he > me:
            if he - me != 1:
                total_score_p1 += 6
        if he < me:
            if me - he == 1:
                total_score_p1 += 6

        total_score_p1 += me - ord("@")




    for line in lines:
        he, iShould = line.split(" ")

        if iShould == "X":
            if he == "A":
                total_score_p2 += 3
            elif he == "B":
                total_score_p2 += 1
            elif he == "C":
                total_score_p2 += 2
        elif iShould == "Y":
            total_score_p2 += ord(he) - ord("@") + 3
        elif iShould == "Z":
            if he == "A":
                total_score_p2 += 8
            elif he == "B":
                total_score_p2 += 9
            elif he == "C":
                total_score_p2 += 7

    return total_score_p1, total_score_p2


def test_day_2():
     assert day_2("test.txt") == (15, 12)


test_day_2()

p1, p2 = day_2("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)

import pytest

def day_2(filename):
    lines = [l.strip() for l in open(filename)]

    total_score_p1 = 0
    total_score_p2 = 0

    # Part 1
    # A - X = Rock
    # B - Y = Paper
    # C - Z = Scissors
    # X - A = 23

    for line in lines:
        chars = line.split(" ")

        game = 0
        score = 0

        he = ord(chars[0])
        me = ord(chars[1]) - 23

        if he == me:
            game = 3
        if he > me:
            if he - me == 1:
                game = 0
            else:
                game = 6
        if he < me:
            if me - he == 1:
                game = 6
            else:
                game = 0

        score = ord(chars[1]) - ord("X") + 1

        total_score_p1 += game + score


    # Part 2
    # X - Lose
    # Y - Draw
    # Z - Win

    counter = 0

    for line in lines:
        chars = line.split(" ")

        game = 0
        score = 0

        counter += 1
        if counter > 3:
            exit

        he = ord(chars[0])

        if chars[1] == "X":
            game = 0
            if chars[0] == "A":
                score = 3
            elif chars[0] == "B":
                score = 1
            elif chars[0] == "C":
                score = 2
        if chars[1] == "Y":
            game = 3
            score = ord(chars[0]) - ord("A") + 1
        if chars[1] == "Z":
            game = 6
            if chars[0] == "A":
                score = 2
            elif chars[0] == "B":
                score = 3
            elif chars[0] == "C":
                score = 1

        total_score_p2 += game + score

    return total_score_p1, total_score_p2


def test_day_2():
     assert day_2("test.txt") == (15, 12)


test_day_2()

p1, p2 = day_2("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)

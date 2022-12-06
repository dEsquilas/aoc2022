import pytest


def get_first_marker(input, default_offset = 4):
    offset = default_offset
    while offset < len(input):
        current = input[offset-default_offset:offset]
        counter = {i: current.count(i) for i in current}
        if len(counter) == default_offset:
            return offset
        offset += 1

    return -1


def day_6(filename):

    # Part 1
    input = open(filename).read()
    output_p1 = get_first_marker(input)

    # Part 2
    output_p2 = get_first_marker(input, 14)

    return output_p1, output_p2


def test_day_6():
    # Part 1
    assert get_first_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert get_first_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert get_first_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert get_first_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert get_first_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    # Part 2
    assert get_first_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert get_first_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert get_first_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert get_first_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert get_first_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26


test_day_6()

p1, p2 = day_6("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

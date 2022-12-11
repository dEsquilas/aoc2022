import pytest
import copy
from parse import parse

class Monkey:
    def __init__(self, data):
        values = parse(
            "Monkey {}: Starting items: {} Operation: new = old {} Test: divisible by {}  If true: throw to monkey {}  If false: throw to monkey {}",
            data)

        operation = values[2].split(" ")

        self.id = int(values[0])
        self.items = [int(l) for l in values[1].split(",")]
        self.operation_symbol = operation[0]

        if "old" in operation[1]:
            self.operation_number_is_old = True
            self.operation_number = 0
        else:
            self.operation_number_is_old = False
            self.operation_number = int(operation[1])

        self.test = int(values[3])
        self.isTrue = int(values[4])
        self.isFalse = int(values[5])

        self.items_inspected = 0


    def execute(self, common=False):

        self.items_inspected += 1

        current_item = self.items.pop(0)

        item_with_worry_level = 0
        if self.operation_number_is_old:
            self.operation_number = current_item

        if "*" in self.operation_symbol:
            item_with_worry_level = (current_item * self.operation_number)
        elif "+" in self.operation_symbol:
            item_with_worry_level = (current_item + self.operation_number)
        else:
            print("Operation not found: ", self.operation_symbol)
            exit()

        # Part 1
        if not common:
            item_with_worry_level //= 3
            if item_with_worry_level % self.test == 0:
                return item_with_worry_level, self.isTrue
            else:
                return item_with_worry_level, self.isFalse
        # Part 2
        else:
            rest = item_with_worry_level % common

            if rest % self.test == 0:
                return rest, self.isTrue
            else:
                return rest, self.isFalse

    def debug2(self):
        print("Monkey", self.id, self.items, self.items_inspected)

    def debug(self):
        print(self.id, self.items_inspected, self.items, self.operation_symbol, self.operation_number_is_old, self.operation_number, self.test, self.isTrue, self.isFalse)


def day_11(filename):

    monkeys_dict = {}

    lines = [l.strip().replace("\n", "").replace("  ", " ") for l in open(filename).read().split("\n\n")]

    for line in lines:
        monkey = Monkey(line)
        monkeys_dict[monkey.id] = monkey

    tmp_monkeys_dict = copy.deepcopy(monkeys_dict)

    common = 1

    for id, monkey in monkeys_dict.items():
        common *= monkey.test

    results = []

    for j in range(2):
        monkeys_dict = copy.deepcopy(tmp_monkeys_dict)
        cycles = 20
        if j == 1:
            cycles = 10000;

        for i in range(cycles):
            for id, monkey in monkeys_dict.items():
                for i in range(len(monkey.items)):
                    if j == 0:
                        item_to_handle, to_monkey = monkey.execute()
                    else:
                        item_to_handle, to_monkey = monkey.execute(common)
                    monkeys_dict[to_monkey].items.append(item_to_handle)

        items_inspected_per_monkey= []
        for id, monkey in monkeys_dict.items():
            items_inspected_per_monkey.append(monkey.items_inspected)

        items_inspected_per_monkey.sort(reverse=True)
        results.append(items_inspected_per_monkey[0] * items_inspected_per_monkey[1])

    return results


def test_day_11():
    assert day_11("test.txt") == [10605, 2713310158]


p1, p2 = day_11("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)


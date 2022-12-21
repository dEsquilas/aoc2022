import pytest
import copy
from collections import OrderedDict
from parse import parse
from pprint import pprint


def shortest_path(paths, to_node, node_index):

    new_paths = []

    for path in paths:
        last_node = path[-1]
        for child in node_index[last_node]:
            if child == to_node:
                path.append(child)
                return path
            elif child not in path:
                current_path = copy.deepcopy(path)
                current_path.append(child)
                new_paths.append(current_path)

    return shortest_path(new_paths, to_node, node_index)


def explore_distances(visited, destinations, distances, current_time):

    new_visited = []

    pprint(visited)

    if current_time > 30:
        return visited

    else:
        for current_visited_stack in visited:
            last_visited_node = current_visited_stack[-1]
            for next_node in destinations:
                if next_node not in current_visited_stack:
                    n = copy.deepcopy(current_visited_stack)
                    pprint("N1")
                    pprint(n)
                    n.append(next_node)
                    pprint("N2")
                    pprint(n)

                    if (last_visited_node, next_node) in distances:
                        current_distance = distances[(last_visited_node, next_node)]
                    else:
                        current_distance = distances[(next_node, last_visited_node)]

                    to_add = explore_distances(n, destinations, distances, current_time + current_distance)
                    new_visited.append(to_add)

    return new_visited




def day_16(filename):

    lines = [l.strip() for l in open(filename).readlines()]

    valves = {}
    flow_rates = {}
    positive_flow_rates = {}
    destinations = []
    valves_with_flow = {}

    for l in lines:

        l = l.replace("tunnels", "tunnel").replace("valves", "valve").replace("leads", "lead")
        valve, flow_rate, valve_to = parse("Valve {} has flow rate={}; tunnel lead to valve {}", l)
        valves[valve] = valve_to.split(", ")
        flow_rates[valve] = int(flow_rate)
        if flow_rates[valve] > 0:
            destinations.append(valve)
            positive_flow_rates[valve] = flow_rates[valve]

    max_pression = 0

    distances = {}

    for current_flow, destination in enumerate(positive_flow_rates):
        path = shortest_path([["AA"]], destination, valves)
        distances[("AA", destination)] = len(path)

    for current_flow, origin in enumerate(positive_flow_rates):
        for sub_current_flow, destination in enumerate(positive_flow_rates):
            if not ((origin, destination) in distances or (destination, origin) in distances):
                path = shortest_path([[origin]], destination, valves)
                distances[(origin, destination)] = len(path)

    current_time = 0
    visited = [["AA"]]

    all_visited = explore_distances(visited, destinations, distances, current_time)

    pprint(all_visited)

    exit()

    # for current_flow, index in enumerate(positive_flow_rates):
    #
    #     current_time = 0
    #     current_visited_valves = set()
    #     current_visited_valves.add(index)
    #     non_visited_valves = set()
    #
    #     for cf, subindex in enumerate(positive_flow_rates):
    #         if subindex != index:
    #             non_visited_valves.add(subindex)
    #
    #     visited_sets = []
    #
    #
    #
    #
    #
    #     print("Valve", current_flow, index)
    #     path = shortest_path(origin, index, valves)
    #     exit()


    path = shortest_path(origin, "CC", valves)

    pprint(path)
    exit()


    return 1651, 0


def test_day_16():
    assert day_16("test.txt") == (1651, 0)


test_day_16()
exit()
p1, p2 = day_16("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

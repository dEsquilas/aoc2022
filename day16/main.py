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

class Way:
    def __init__(self):
        self.time = 0
        self.visited = set()
        self.last_visited = ""


def explore_distances(visited, destinations, distances):

    new_visited = []

    #pprint("Starting finding")

    new_added = False

    for current_way in visited:


        #print(vars(current_way))

        for way_to_go in destinations:

            if way_to_go not in current_way.visited:

                new_way_to_go = copy.deepcopy(current_way)

                if (current_way.last_visited, way_to_go) in distances:
                    current_distance = distances[(current_way.last_visited, way_to_go)]
                else:
                    current_distance = distances[(way_to_go, current_way.last_visited)]


                if current_way.time + current_distance < 30:
                    new_way_to_go.last_visited = way_to_go
                    new_way_to_go.visited.add(way_to_go)
                    new_way_to_go.time += current_distance
                    new_visited.append(new_way_to_go)
                    new_added = True
                    #print("here")
                else:
                    #print("orhere")
                    new_visited.append(new_way_to_go)

    pprint(len(new_visited))

    if not new_added:
        return visited
    else:
        return explore_distances(new_visited, destinations, distances)


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


    # origin = Way()
    # origin.visited.add("AA")
    # origin.last_visited = "AA"


    # all_visited = explore_distances([origin], destinations, distances)
    #
    # max_pressure = 0
    #
    # for v in all_visited:
    #     current_pressure = 0
    #     for node in v.visited:
    #         current_pressure += flow_rates[node]
    #     max_pressure = max(current_pressure, max_pressure)

    current_set = set()
    current_set.add("AA")

    # calculate what valve get more pressure on less time

    current_valve = "AA"
    visited_valves = set()
    visited_valves.add("AA")
    remaining_time = 30
    pressure_in_all_time = 0

    while remaining_time > 0:

        best_option = 0
        best_valve = ""
        best_time = 0

        for destination in destinations:
            if destination not in visited_valves:
                if (current_valve, destination) in distances:
                    current_distance = distances[(current_valve, destination)]
                else:
                    current_distance = distances[(destination, current_valve)]
                pressure_in_rest_time = flow_rates[destination] * (remaining_time - current_distance)

                print(pressure_in_rest_time, destination)

                if pressure_in_rest_time > best_option:
                    best_option = pressure_in_rest_time
                    best_valve = destination
                    best_time = current_distance

        visited_valves.add(best_valve)
        current_valve = best_valve
        pressure_in_all_time += best_option
        remaining_time -= current_distance
        print("Best option", best_valve, best_option, remaining_time)


    pprint(pressure_in_all_time)
    exit()



    return 81, 0


def test_day_16():
    assert day_16("test.txt") == (81, 0)


test_day_16()
exit()
p1, p2 = day_16("input.txt")

print("Part 1:", p1)
print("Part 2:", p2)

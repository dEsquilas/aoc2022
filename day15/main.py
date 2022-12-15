import pytest
from parse import parse


def day_15(filename, y_rect):

    if y_rect == 10:
        max_range = 20
    else:
        max_range = 4000000

    lines = [l.strip() for l in open(filename).readlines()]
    sensors = []
    beacons = []

    for l in lines:
        sx,sy,bx,by = parse("Sensor at x={}, y={}: closest beacon is at x={}, y={}", l)
        sensors.append((int(sx), int(sy)))
        beacons.append((int(bx), int(by)))

    covered_positions = {}

    for i in range(len(sensors)):
        dx = abs(sensors[i][0] - beacons[i][0])
        dy = abs(sensors[i][1] - beacons[i][1])

        distance = dx + dy

        distance_sensor_y_rect = abs(sensors[i][1] - y_rect)

        if distance_sensor_y_rect <= distance:

            y_distance = sensors[i][1] - y_rect
            if y_distance > distance:
                current = (sensors[i][0], sensors[i][1] + y_distance)
            else:
                current = (sensors[i][0], sensors[i][1] - y_distance)

            for x in range(distance - distance_sensor_y_rect+1):
                covered_positions[current[0] + x, current[1]] = True
                covered_positions[current[0] - x, current[1]] = True

            covered_positions[current] = True

    for b in beacons:
        if b in covered_positions.keys():
            covered_positions.pop(b)

    for s in sensors:
        if s in covered_positions.keys():
            covered_positions.pop(s)

    point_found = None

    for i in range(len(sensors)):

        if point_found is not None:
            break

        dx = abs(sensors[i][0] - beacons[i][0])
        dy = abs(sensors[i][1] - beacons[i][1])

        distance = dx + dy + 1

        cx = distance
        cy = 0

        points_to_check = set()

        while cx >= 0:
            points_to_check.add((sensors[i][0] + cx, sensors[i][1] + cy))
            points_to_check.add((sensors[i][0] - cx, sensors[i][1] + cy))
            points_to_check.add((sensors[i][0] + cx, sensors[i][1] - cy))
            points_to_check.add((sensors[i][0] - cx, sensors[i][1] - cy))
            cy += 1
            cx -= 1

        for point in points_to_check:

            if 0 <= point[0] <= max_range and 0 <= point[1] <= max_range:
                found = False
                for j in range(len(sensors)):
                    if j != i:
                        bdx = abs(sensors[j][0] - beacons[j][0])
                        bdy = abs(sensors[j][1] - beacons[j][1])

                        pdx = abs(sensors[j][0] - point[0])
                        pdy = abs(sensors[j][1] - point[1])

                        current_distance_to_beacon = bdx + bdy
                        current_distance_to_point = pdx + pdy

                        if current_distance_to_point <= current_distance_to_beacon:
                            found = True
                            break

                if not found:
                    point_found = point
                    break

    return len(covered_positions), point_found[0] * 4000000 + point_found[1]


def test_day_15():
    assert day_15("test.txt", 10) == (26, 56000011)


test_day_15()
p1, p2 = day_15("input.txt", 2000000)

print("Part 1:", p1)
print("Part 2:", p2)

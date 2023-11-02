"""
Copyright 2022 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from math import inf
from typing import (
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day15(DayMeta):
    """
    Advent of Code 2022, Day 15
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_15.txt')

        return [
            str(cls.compute_part_1(raw_data, row=2000000)),
            str(cls.compute_part_2(raw_data))
        ]

    @classmethod
    def compute_part_1(cls, data: List[str], row: int):
        """
        Parse the data and compute for Day 15.
        :param data: The data from Advent of Code.
        :param row: The row to process here.
        :returns: The result for Part 1.
        """
        parsed_data = cls._parse(data)

        min_x, max_x = inf, -inf
        for x_val, y_val, r_val in parsed_data:
            diff_y = abs(row - y_val)
            if diff_y > r_val:
                continue
            diff_x = abs(r_val - diff_y)
            min_x = min(x_val - diff_x, min_x)
            max_x = max(x_val + diff_x, max_x)

        return max_x - min_x

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 15.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        parsed_data = cls._parse(data)
        for y_pos in range(4000000):
            if x_result := cls._find_beacon(parsed_data, y_pos):
                return x_result * 4000000 + y_pos

        return -1

    @classmethod
    def _find_beacon(cls, data: List[Tuple[int, int, int]], y_pos: int):
        ranges = []

        for sensor_x, sensor_y, radius in data:
            diff_y = abs(y_pos - sensor_y)
            if diff_y > radius:
                continue
            diff_x = radius - diff_y
            ranges.append((sensor_x - diff_x, sensor_x + diff_x))

        ranges.sort()
        min_x, max_x = ranges[0]

        for x_start, x_end in ranges[1:]:
            test_min = min_x - 1
            test_max = max_x + 1

            if x_start < test_min and x_end < test_min:
                return test_min

            if x_start > test_max and x_end > test_max:
                return test_max

            min_x = min(x_start, min_x)
            max_x = max(x_end, max_x)

        return False

    @classmethod
    def _parse(cls, data: List[str]) -> List[Tuple[int, int, int]]:
        pair_details = []

        for data_entry in data:
            sensor, beacon = cls._parse_coords_from_line(data_entry)
            radius = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            pair_details.append((sensor[0], sensor[1], radius))

        return pair_details

    @classmethod
    def _parse_coords_from_line(
            cls,
            data_line: str
    ) -> Tuple[Tuple[int, int], Tuple[int, int]]:

        data_line = data_line.replace('Sensor at ', '')
        data_line = data_line.replace(' closest beacon is at ', '')
        data_line = data_line.replace(' ', '')
        data_line = data_line.replace('x=', '').replace('y=', '')
        raw_sensor, raw_beacon = data_line.split(':')
        raw_sensor = raw_sensor.split(',')
        raw_beacon = raw_beacon.split(',')

        return (int(raw_sensor[0]), int(raw_sensor[1])), \
            (int(raw_beacon[0]), int(raw_beacon[1]))

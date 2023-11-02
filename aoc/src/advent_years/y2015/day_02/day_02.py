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

from typing import (
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day02(DayMeta):
    """
    Advent of Code 2015, Day 02
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_02.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """

        result = 0
        for data_entry in data:
            length, width, height = cls._parse_entry(data_entry)
            result += cls._compute_size(length, width, height)
        return result

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        result = 0

        for data_entry in data:
            sizes = sorted(cls._parse_entry(data_entry))
            result += (2 * sizes[0]) + (2 * sizes[1])
            result += sizes[0] * sizes[1] * sizes[2]

        return result

    @classmethod
    def _compute_size(cls, length: int, width: int, height: int):
        side_a = length * width
        side_b = width * height
        side_c = height * length
        sides = [side_a, side_b, side_c]
        smallest = min(sides)

        result = 0

        for side in sides:
            result += 2 * side

        return result + smallest

    @classmethod
    def _parse_entry(cls, data_entry: str) -> Tuple[int, int, int]:
        raw_results = data_entry.split('x')
        return (
            int(raw_results[0]),
            int(raw_results[1]),
            int(raw_results[2]),
        )

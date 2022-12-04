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
    Set,
    Tuple,
)

from ..day_meta import DayMeta


class Day04(DayMeta):
    """
    Advent of Code 2022, Day 04
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_04.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, raw_data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param raw_data: The raw data from Advent of Code
        :returns: The result for Part 1
        """

        results = 0
        for raw_data_entry in raw_data:
            # Get the groups, and make the set ranges
            group_a, group_b = cls._split_pairs(raw_data_entry)
            group_a = cls._get_range_points(group_a)
            group_b = cls._get_range_points(group_b)
            set_a = cls._get_set_from_range(group_a)
            set_b = cls._get_set_from_range(group_b)
            # compare
            if set_a.issuperset(set_b) or set_a.issubset(set_b):
                results += 1

        return results

    @classmethod
    def compute_part_2(cls, raw_data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param raw_data: The raw data from Advent of Code
        :returns: The result for Part 2
        """

        results = 0
        for raw_data_entry in raw_data:
            # Get the groups, and make the set ranges
            group_a, group_b = cls._split_pairs(raw_data_entry)
            group_a = cls._get_range_points(group_a)
            group_b = cls._get_range_points(group_b)
            set_a = cls._get_set_from_range(group_a)
            set_b = cls._get_set_from_range(group_b)
            # compare
            intersection_set = set_a.intersection(set_b)
            if len(intersection_set) > 0:
                results += 1

        return results

    @classmethod
    def _get_range_points(cls, range_data: str) -> Tuple[int, int]:
        """

        :param range_data:
        :return:
        """
        start, end = range_data.split('-')
        return int(start), int(end)

    @classmethod
    def _get_set_from_range(cls, range_points: Tuple[int, int]) -> Set[int]:
        """

        :param range_points:
        :return:
        """
        start, end = range_points[0], range_points[1] + 1
        return set(range(start, end))

    @classmethod
    def _split_pairs(cls, raw_data: str) -> (str, str):
        """

        :param raw_data:
        :return:
        """
        raw_data_objects = raw_data.split(',')
        return raw_data_objects[0], raw_data_objects[1]

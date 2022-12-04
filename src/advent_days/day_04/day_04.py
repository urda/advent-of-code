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
            set_a, set_b = cls._parse_entry(raw_data_entry)
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
            set_a, set_b = cls._parse_entry(raw_data_entry)
            if len(set_a.intersection(set_b)) > 0:
                results += 1

        return results

    @classmethod
    def _get_range_points(cls, range_data: str) -> Tuple[int, int]:
        """
        Given a raw string for a pair, make a tuple of ints from it.

        :param range_data: The range as a string from the input.
        :return: The pair split into ints, parsed
        """

        start, end = range_data.split('-')
        return int(start), int(end)

    @classmethod
    def _get_set_from_range(cls, range_points: Tuple[int, int]) -> Set[int]:
        """
        Given a tuple of ints, make a set from the range of the ints.

        :param range_points: The range as ints, from low to high
        :return: A set of the range.
        """

        start, end = range_points[0], range_points[1] + 1
        return set(range(start, end))

    @classmethod
    def _parse_entry(cls, raw_data: str) -> Tuple[Set[int], Set[int]]:
        """
        Parse a string from the data file into int literals.

        :param raw_data: The raw data file line from the input.
        :return: A tuple of the pairs as sets.
        """

        group_a, group_b = cls._split_pairs(raw_data)
        group_a = cls._get_range_points(group_a)
        group_b = cls._get_range_points(group_b)
        return (
            cls._get_set_from_range(group_a),
            cls._get_set_from_range(group_b),
        )

    @classmethod
    def _split_pairs(cls, raw_data: str) -> Tuple[str, str]:
        """
        Given the line of data, split the pairs into strings.

        :param raw_data: The raw data file line from the input.
        :return: A tuple of strings
        """

        raw_data_objects = raw_data.split(',')
        return raw_data_objects[0], raw_data_objects[1]

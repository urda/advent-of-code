"""
Copyright 2023 Peter Urda

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
    Dict,
    List,
)

from .bitmiser import BitMiser
from ..day_meta import DayMeta


class Day07(DayMeta):
    """
    Advent of Code 2015, Day 07
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_07.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data) -> int:
        """
        Parse the data and compute for Day 07.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        calculations = cls._parse(data)
        bitmiser = BitMiser(calculations)
        return bitmiser.calculate('a')

    @classmethod
    def compute_part_2(cls, data) -> int:
        """
        Parse the data and compute for Day 07.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        calculations = cls._parse(data)
        calculations['b'] = [str(cls.compute_part_1(data))]
        bitmiser = BitMiser(calculations)
        return bitmiser.calculate('a')

    @classmethod
    def _parse(cls, data: List[str]) -> Dict[str, list]:
        results = {}

        for data_entry in data:
            (ops, res) = data_entry.split('->')
            results[res.strip()] = ops.strip().split(' ')

        return results

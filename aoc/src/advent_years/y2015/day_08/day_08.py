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
    List,
    Tuple,
)

from .sleigh_list_entry import SleighListEntry
from ..day_meta import DayMeta


class Day08(DayMeta):
    """
    Advent of Code 2015, Day 08
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_08.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 08.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        _sum_code, _sum_mem, _ = cls._compute_all_parts(data)
        return _sum_code - _sum_mem

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 08.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        _sum_code, _, _sum_super = cls._compute_all_parts(data)
        return _sum_super - _sum_code

    @classmethod
    def _compute_all_parts(cls, data: List[str]) -> Tuple[int, int, int]:
        entries = cls._parse(data)

        _sum_code = 0
        _sum_mem = 0
        _sum_super = 0

        for entry in entries:
            _sum_code += entry.code_length
            _sum_mem += entry.memory_length
            _sum_super += entry.super_escaped_length

        return _sum_code, _sum_mem, _sum_super

    @classmethod
    def _parse(cls, data: List[str]) -> List[SleighListEntry]:
        return [SleighListEntry(entry) for entry in data]

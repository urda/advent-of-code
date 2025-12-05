"""
Copyright 2025 Peter Urda

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

from typing import List

from .safe_dial import SafeDial
from ..day_meta import DayMeta


class Day01(DayMeta):
    """
    Advent of Code 2025, Day 01
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_01.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 02.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        zero_count = 0
        my_safe = SafeDial()

        for rot_instruction in data:
            pos = my_safe.spin_dial(rot_instruction)
            if pos == 0:
                zero_count += 1

        return zero_count

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 02.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        zero_count = 0
        my_safe = SafeDial()

        for rot_instruction in data:
            zero_count += my_safe.spin_zero(rot_instruction)
        return zero_count

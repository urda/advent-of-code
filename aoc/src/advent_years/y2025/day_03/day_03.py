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

from ..day_meta import DayMeta


class Day03(DayMeta):
    """
    Advent of Code 2025, Day 03
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_03.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 03.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        joltage = 0

        for bank in data:
            joltage += cls._max_two_digit(bank)

        return joltage

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 03.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        joltage = 0

        for bank in data:
            joltage += cls._max_digits(bank)

        return joltage

    @classmethod
    def _max_two_digit(cls, bank: str) -> int:
        best = -1
        max_right = -1

        for ch in reversed(bank):
            curr_digit = int(ch)

            # Can we check for the best?
            if max_right >= 0:
                best = max(best, curr_digit * 10 + max_right)
            max_right = max(max_right, curr_digit)

        return best

    @classmethod
    def _max_digits(cls, bank: str) -> int:
        drop = len(bank) - 12
        stack = []
        for ch in bank:
            while drop and stack and stack[-1] < ch:
                stack.pop()
                drop -= 1
            stack.append(ch)
        return int(''.join(stack[:12]))

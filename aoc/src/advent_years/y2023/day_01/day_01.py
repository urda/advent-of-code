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

import sys
from typing import List

from ..day_meta import DayMeta


class Day01(DayMeta):
    """
    Advent of Code 2023, Day 01
    """

    _known_numbers = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

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
        Parse the data and compute for Day 01.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._parse_lines(data, False)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 01.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._parse_lines(data, True)

    @classmethod
    def _parse_line(cls, data: str, word_check: bool) -> int:
        first_value = (sys.maxsize, None)
        last_value = (-1, None)

        if word_check:
            for word, word_value in cls._known_numbers.items():
                if word not in data:
                    continue
                # Word is in the data line, where is it?
                earliest_idx = data.index(word)
                latest_idx = data.rfind(word)

                if earliest_idx < first_value[0]:
                    first_value = (earliest_idx, word_value)
                if latest_idx > last_value[0]:
                    last_value = (latest_idx, word_value)

        # Search the data line for integers, and report into result
        for idx, char_val in enumerate(data):
            if char_val.isnumeric():
                if idx < first_value[0]:
                    first_value = [idx, int(char_val)]
                if idx > last_value[0]:
                    last_value = [idx, int(char_val)]

        computed_value = int(f'{first_value[1]}{last_value[1]}')
        return computed_value

    @classmethod
    def _parse_lines(cls, data: List[str], word_check: bool) -> int:
        result = 0
        for data_line in data:
            result += cls._parse_line(data_line, word_check)
        return result

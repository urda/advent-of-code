"""
Copyright 2021 Peter Urda

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

from .day_meta import DayMeta


class Day01(DayMeta):
    """
    Advent Day 01
    """

    _data_file = 'day_01.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_answer = cls.compute_part_1(cls._get_lines())
        part_2_answer = cls.compute_part_2(cls._get_lines())

        return [
            f'Part 01 Determined: {part_1_answer}',
            f'Part 02 Determined: {part_2_answer}',
        ]

    @classmethod
    def _get_lines(cls) -> List[int]:
        lines = []
        with open(
                cls.build_data_file_path(cls._data_file),
                'r',
                encoding='utf-8',
        ) as data_file:
            for line in data_file:
                try:
                    lines.append(int(line))
                except ValueError as error:
                    raise error
        return lines

    @classmethod
    def compute_part_1(cls, lines: List[int]) -> int:
        """
        Compute the answer to part 1 for Day 01.

        :param lines: The input lines of integers to process.
        :return: The answer to part 1 for Day 01.
        """

        # Set the first seen value to the smallest value possible for
        # this system, then set counter to -1 so first value sets counter to 0
        increased_count = -1
        previous_value = ~sys.maxsize

        for current_value in lines:
            if current_value > previous_value:
                increased_count += 1
            previous_value = current_value

        return increased_count

    @classmethod
    def compute_part_2(cls, lines: List[int]) -> int:
        """
        Compute the answer to part 2 for Day 01.

        :param lines: The input lines of integers to process.
        :return: The answer to part 2 for Day 01.
        """

        rolling_window_size = 3
        rolling_window = []
        increased_count = -1
        previous_value = ~sys.maxsize

        for loading_value in lines:
            rolling_window.append(loading_value)

            # If we don't have three entries to read, keep loading
            if len(rolling_window) < rolling_window_size:
                continue

            current_total = sum(rolling_window)

            if current_total > previous_value:
                increased_count += 1

            previous_value = current_total
            rolling_window.pop(0)

        return increased_count

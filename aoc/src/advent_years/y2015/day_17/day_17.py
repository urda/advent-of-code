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
from itertools import combinations
from typing import List

from ..day_meta import DayMeta


class Day17(DayMeta):
    """
    Advent of Code 2015, Day 17
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_int('day_17.txt')
        target = 150

        return [
            str(cls.compute_part_1(raw_data, target)),
            str(cls.compute_part_2(raw_data, target)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[int], target: int) -> int:
        """
        Parse the data and compute for Day 17.
        :param data: The data from Advent of Code.
        :param target: The target liters for this part.
        :returns: The result for Part 1.
        """
        result = 0
        for r in range(1, len(data) + 1):
            for combination in combinations(data, r):
                if sum(combination) == target:
                    result += 1
        return result

    @classmethod
    def compute_part_2(cls, data: List[int], target: int) -> int:
        """
        Parse the data and compute for Day 17.
        :param data: The data from Advent of Code.
        :param target: The target liters for this part.
        :returns: The result for Part 2.
        """
        results = []
        min_size = sys.maxsize
        for r in range(1, len(data) + 1):
            for combination in combinations(data, r):
                if len(combination) > min_size:
                    break
                if sum(combination) == target:
                    min_size = len(combination)
                    results.append(combination)
        return len(results)

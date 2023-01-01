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
from collections import Counter
from functools import lru_cache
from typing import (
    List,
    Tuple,
)

from .day_meta import DayMeta


class Day07(DayMeta):
    """
    Advent Day 07
    """

    _data_file = 'day_07.txt'

    _data_delimiter = ','

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_result = \
            cls.perform_work(cls.get_csv_line_as_integer_list(cls._data_file),
                             False)[0]
        part_2_result = \
            cls.perform_work(cls.get_csv_line_as_integer_list(cls._data_file),
                             True)[0]

        return [
            'Part 1:',
            f'Determined: {part_1_result}',
            '---',
            'Part 2:',
            f'Determined: {part_2_result}',
        ]

    @classmethod
    @lru_cache(maxsize=None)
    def get_complex_fuel_usage(cls, distance_to_cover: int) -> int:
        """
        Compute the complex fuel requirements.

        As it turns out, crab submarine engines don't burn fuel at a constant
        rate. Instead, each change of 1 step in horizontal position costs 1
        more unit of fuel than the last: the first step costs 1, the second
        step costs 2, the third step costs 3, and so on.

        :param distance_to_cover: The distance the crab sub covers.
        :return: The fuel used to cover that distance.
        """
        fuel = 0
        for offset in range(1, distance_to_cover + 1):
            fuel += offset
        return fuel

    @classmethod
    def perform_work(
            cls,
            raw_crabs: List[int],
            complex_fuel_spend: bool = False
    ) -> Tuple[int, int]:
        """
        Perform work needed to get the crab subs aligned and get the answer.

        :param raw_crabs: The crab subs to align with.
        :param complex_fuel_spend: Set to 'True' if computation should use the
                                   more-complex fuel calculations.
        :return: A tuple with two values: (fuel spent, alignment level)
        """

        raw_crab_sorted = sorted(raw_crabs)
        min_value = raw_crab_sorted[0]
        max_value = raw_crab_sorted[-1]

        crab_counter = Counter(raw_crab_sorted)

        min_fuel_seen = sys.maxsize
        alignment_result = None

        # pylint: disable=invalid-name
        for x in range(min_value, max_value + 1):
            total_fuel_spent = 0
            for crabs in crab_counter.items():
                if complex_fuel_spend:
                    fuel_distance = abs(crabs[0] - x)
                    fuel_spent_for_all = \
                        cls.get_complex_fuel_usage(fuel_distance) * crabs[1]
                    total_fuel_spent += fuel_spent_for_all
                else:
                    fuel_spent = abs(crabs[0] - x)
                    fuel_spent_for_all = fuel_spent * crabs[1]
                    total_fuel_spent += fuel_spent_for_all

            if total_fuel_spent < min_fuel_seen:
                min_fuel_seen = total_fuel_spent
                alignment_result = (total_fuel_spent, x)

        if not alignment_result:
            raise ValueError('Unable to shuffle crabs!')

        return alignment_result

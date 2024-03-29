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

from collections import Counter
from typing import List

from .day_meta import DayMeta


class Day06(DayMeta):
    """
    Advent Day 06
    """

    _data_file = 'day_06.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_result = cls.perform_work(
            cls.get_csv_line_as_integer_list(cls._data_file),
            80,
        )
        part_2_result = cls.perform_work(
            cls.get_csv_line_as_integer_list(cls._data_file),
            256,
        )

        return [
            'Part 1:',
            f'Determined fish population: {part_1_result}',
            '---',
            'Part 2:',
            f'Determined fish population: {part_2_result}',
        ]

    @classmethod
    def _cycle_fish(cls, fish_buckets):
        # Extract fish at bucket zero
        day_zero_fish = fish_buckets[0]
        # Slice everyone but day zero
        fish = fish_buckets[1:]
        # Put the fish at the end (these are the new fish)
        fish.append(day_zero_fish)
        # Put the current fish in their "reset" value bucket
        fish[6] += day_zero_fish
        return fish

    @classmethod
    def perform_work(cls, fish_data: List[int], day_limit: int) -> int:
        """
        Perform the work for this day's advent challenge.

        :param fish_data: The fish data from the challenge.
        :param day_limit: The number of days to compute.
        :return: The number of fish in the simulation.
        """
        fish_buckets = [0] * 9
        for key, value in Counter(fish_data).items():
            fish_buckets[key] = value

        for _ in range(day_limit):
            new_fish_buckets = cls._cycle_fish(fish_buckets)
            fish_buckets = new_fish_buckets[:]

        return sum(fish_buckets)

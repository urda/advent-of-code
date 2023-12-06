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

import re
from typing import List

from ..day_meta import DayMeta


class Day06(DayMeta):
    """
    Advent of Code 2023, Day 06
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_06.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 06.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        time_num = cls._parse_numbers(data[0], False)
        distance_num = cls._parse_numbers(data[1], False)
        return cls._run_races(time_num, distance_num)

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 06.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        time_num = cls._parse_numbers(data[0], True)
        distance_num = cls._parse_numbers(data[1], True)
        return cls._run_races(time_num, distance_num)

    @classmethod
    def _dirty_multiply_list(cls, input_list: List[int]) -> int:
        """
        Take all the values in a list and multiply them together.
        """
        result = 1
        for x in input_list:
            result = result * x
        return result

    @classmethod
    def _get_methods(cls, time_val: int, distance_val: int, button_time: int):
        """
        Get the number of methods you can beat the record.
        """
        time_remaining = time_val - button_time

        if time_remaining <= 0:
            return False

        speed = button_time
        full_distance = speed * time_remaining
        if full_distance > distance_val:
            return True

        return False

    @classmethod
    def _parse_numbers(
            cls,
            data_line: str,
            single_num_mode: bool,
    ) -> List[int]:
        """
        Parse a data line as many numbers, or a single big number.
        """
        if single_num_mode:
            result = [int(
                re.sub(
                    r'(\d)\s+(\d)',
                    r'\1\2',
                    data_line.split(':')[1].strip()
                )
            )]
        else:
            result = [
                int(x) for x in data_line.split(':')[1].split(' ')
                if len(x) > 0
            ]
        return result

    @classmethod
    def _run_races(cls, time_num: List[int], distance_num: List[int]) -> int:
        """
        Run the races given the input time and distance pairs.
        """
        results = []
        for race_idx in range(len(time_num)):
            curr_time = time_num[race_idx]
            curr_distance = distance_num[race_idx]

            winners = 0
            for x_test in range(1, curr_time):
                winner = cls._get_methods(curr_time, curr_distance, x_test)
                if winner:
                    winners += 1

            results.append(winners)

        return cls._dirty_multiply_list(results)

"""
Copyright 2022 Peter Urda

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


class Day01(DayMeta):
    """
    Advent of Code 2015, Day 01
    """

    _UP = '('
    _DOWN = ')'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_01.txt')[0]

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: str) -> int:
        """
        Parse the data and convert into an understood format and compute.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        curr_floor = 0

        for data_char in data:
            curr_floor = cls._step(curr_floor, data_char)

        return curr_floor

    @classmethod
    def compute_part_2(cls, data: str) -> int:
        """
        Parse the data and convert into an understood format and compute.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        curr_floor = 0

        for idx, data_char in enumerate(data):
            curr_floor = cls._step(curr_floor, data_char)

            if curr_floor == -1:
                return idx + 1

        return -1

    @classmethod
    def _step(cls, curr_floor, data_char):
        """
        Move up or down the floors.

        :param curr_floor: The current floor.
        :param data_char: The movement character.
        :return: The new floor id.
        """
        match data_char:
            case cls._UP:
                curr_floor += 1
            case cls._DOWN:
                curr_floor -= 1
            case _:
                raise ValueError

        return curr_floor

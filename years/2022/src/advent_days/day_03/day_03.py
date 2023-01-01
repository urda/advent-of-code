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

from string import (
    ascii_lowercase,
    ascii_uppercase,
)
from typing import (
    Dict,
    List,
)

from ..day_meta import DayMeta


class Day03(DayMeta):
    """
    Advent of Code 2022, Day 03
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_03.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, raw_data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param raw_data: The raw data from Advent of Code
        :returns: The result for Part 1
        """

        score = 0
        for box in raw_data:
            box_a, box_b = cls.split_string(box)
            commons = list(set(box_a).intersection(box_b))

            score += cls.get_scoring_lut()[commons.pop()]

        return score

    @classmethod
    def compute_part_2(cls, raw_data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param raw_data: The raw data from Advent of Code
        :returns: The result for Part 2
        """

        score = 0
        sub_group_id = 0
        sub_set = []
        for box in raw_data:
            sub_set.append(box)
            sub_group_id += 1

            if sub_group_id > 2:
                local_set = set(sub_set[0])
                for local_sub_set in sub_set:
                    local_set = local_set.intersection(local_sub_set)

                score += cls.get_scoring_lut()[local_set.pop()]

                sub_group_id = 0
                sub_set = []

        return score

    @classmethod
    def split_string(cls, data: str) -> (str, str):
        """
        Slice the string in half

        :param data: The single string entry to split
        :return: The string evently split as a tuple
        """
        return (
            data[:len(data) // 2],
            data[len(data) // 2:],
        )

    @classmethod
    def get_scoring_lut(cls) -> Dict[str, int]:
        """
        Build score lookup table.

        :return: A dictionary where the keys are 'chars', the values the score.
        """
        score_lut = {}
        search_space = ascii_lowercase + ascii_uppercase

        for index, char in enumerate(search_space):
            score_lut[char] = index + 1

        return score_lut

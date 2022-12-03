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
            str(cls.parse_data(raw_data)),
            str(cls.parse_data2(raw_data)),
        ]

    @classmethod
    def parse_data(cls, raw_data: List[str]) -> int:
        """
        Parse the data and convert into an understood format.

        :param raw_data: The raw data from Advent of Code
        :returns:
        """

        score = 0
        for box in raw_data:
            box_a, box_b = cls.split_string(box)
            commons = list(set(box_a).intersection(box_b))

            score += cls.get_lut()[commons.pop()]

        return score

    @classmethod
    def parse_data2(cls, raw_data: List[str]) -> int:
        """
        Parse the data and convert into an understood format.

        :param raw_data: The raw data from Advent of Code
        :returns:
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

                score += cls.get_lut()[local_set.pop()]

                sub_group_id = 0
                sub_set = []

        return score

    @classmethod
    def split_string(cls, data: str) -> (str, str):
        return data[:len(data) // 2], data[len(data) // 2:]

    @classmethod
    def get_lut(cls) -> Dict[str, int]:
        results = {}

        start_value = 1
        for char in ascii_lowercase:
            results[char] = start_value
            start_value += 1

        for char in ascii_uppercase:
            results[char] = start_value
            start_value += 1

        return results

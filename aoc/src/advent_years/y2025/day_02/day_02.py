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


class Day02(DayMeta):
    """
    Advent of Code 2025, Day 02
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_string('day_02.txt')
        raw_datas = raw_data.split(',')

        return [
            str(cls.compute_part_1(raw_datas)),
            str(cls.compute_part_2(raw_datas)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 02.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        invalid_ids = 0

        for id_check in data:
            start, end = id_check.split('-')
            start, end = int(start), int(end)

            for x in range(start, end + 1):
                if cls._is_invalid_id(str(x)):
                    invalid_ids += x

        return invalid_ids

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 02.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        invalid_ids = 0

        for id_check in data:
            start, end = id_check.split('-')
            start, end = int(start), int(end)

            for x in range(start, end + 1):
                if cls._is_invalid_repeated(str(x)):
                    invalid_ids += x

        return invalid_ids

    @classmethod
    def _is_invalid_id(cls, val: str) -> bool:
        mid = len(val) // 2
        return len(val) % 2 == 0 and val[:mid] == val[mid:]

    @classmethod
    def _is_invalid_repeated(cls, val: str) -> bool:
        # classic trick: if s is a repetition, it appears inside (s+s)[1:-1]
        return len(val) > 1 and val in (val + val)[1:-1]

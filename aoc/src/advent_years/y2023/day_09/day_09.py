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

from typing import List

from ..day_meta import DayMeta


class Day09(DayMeta):
    """
    Advent of Code 2023, Day 09
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_09.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 09.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._compute_oasis(data, True)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 09.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._compute_oasis(data, False)

    @classmethod
    def _build_sequence(cls, data: List[int]) -> List[int]:
        """
        Build the 'next' sequence of numbers for OASIS.
        """
        results = []
        for idx in range(len(data) - 1):
            results.append(data[idx + 1] - data[idx])
        return results

    @classmethod
    def _compute_oasis(cls, data: List[str], end_cap_mode: bool) -> int:
        """
        Compute the OASIS - Oasis And Sand Instability Sensor
        """
        results = 0
        for data_line in data:
            data_line_int = [int(x) for x in data_line.split(' ')]
            computed = cls._predict_value(data_line_int, end_cap_mode)
            results += computed

        return results

    @classmethod
    def _predict_value(cls, data: List[int], end_cap: bool) -> int:
        """
        Given a list of values which "mode" to predict in, predict a value.
        """
        sub_lists = [data]
        last_seq = data
        while not all(x == 0 for x in last_seq):
            new_seq = cls._build_sequence(last_seq)
            sub_lists.append(new_seq)
            last_seq = new_seq

        last_val = 0
        for curr_seq in reversed(sub_lists):
            if end_cap:
                last_val = last_val + curr_seq[-1]
            else:
                last_val = curr_seq[0] - last_val

        return last_val

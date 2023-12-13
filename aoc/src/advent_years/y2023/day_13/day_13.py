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


class Day13(DayMeta):
    """
    Advent of Code 2023, Day 13
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_13.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 13.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._parse_reflections(data, 0)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 13.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._parse_reflections(data, 1)

    @classmethod
    def _get_mismatched_idx(cls, str_a, str_b) -> List[int]:
        misses = []
        for idx, (val_a, val_b) in enumerate(zip(str_a, str_b)):
            if val_a != val_b:
                misses.append(idx)

        return misses

    @classmethod
    def _parse_reflection(cls, data: List[str], margin: int) -> int:
        """
        Parse a singular reflection data set.
        """
        for row_idx in range(len(data) - 1):
            if cls._reflects(data, row_idx, margin, True):
                return (row_idx + 1) * 100

        for col_idx in range(len(data[0]) - 1):
            if cls._reflects(data, col_idx, margin, False):
                return col_idx + 1

        return 0

    @classmethod
    def _parse_reflections(cls, data: List[str], margin: int) -> int:
        """
        Read the data, and calculate reflections for each data set.
        """
        if data[-1] != '':
            data.append('')

        results = 0
        reflection = []
        for data_line in data:
            if data_line == '':
                results += cls._parse_reflection(reflection, margin)
                reflection = []
            else:
                reflection.append(data_line)

        return results

    @classmethod
    def _reflects(
            cls,
            data: List[str],
            possible_idx: int,
            margin: int,
            row_scan: bool,
    ) -> bool:
        """
        Report if, at the given index location,
        if this data reflects in the columns orientation.
        """
        lower_lim = 0
        upper_lim = len(data) if row_scan else len(data[0])
        check_a = possible_idx
        check_b = possible_idx + 1
        errors = 0

        while (check_a >= lower_lim) and (check_b < upper_lim):
            if row_scan:
                row_a = data[check_a]
                row_b = data[check_b]
            else:
                col_a = []
                col_b = []
                for row_data in data:
                    col_a.append(row_data[check_a])
                    col_b.append(row_data[check_b])
                row_a = ''.join(col_a)
                row_b = ''.join(col_b)

            if row_a != row_b:
                errors += len(cls._get_mismatched_idx(row_a, row_b))
                if errors > margin:
                    return False

            check_a -= 1
            check_b += 1

        return errors == margin

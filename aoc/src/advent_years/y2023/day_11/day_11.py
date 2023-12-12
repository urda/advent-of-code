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

from itertools import combinations
from typing import (
    Dict,
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day11(DayMeta):
    """
    Advent of Code 2023, Day 11
    """

    _SPACE_CHAR = '.'
    _STAR_CHAR = '#'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_11.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 11.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._shortest_paths(data, 2)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 11.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._shortest_paths(data, 1_000_000)

    @classmethod
    def _convert_data(cls, data: List[str]) -> List[List[str]]:
        """
        Bust data into a list of lists.
        """
        new_galaxy = []
        for data_row in data:
            new_row = []
            for char_value in data_row:
                new_row.append(char_value)
            new_galaxy.append(new_row)
        return new_galaxy

    @classmethod
    def _scan_galaxy(
            cls,
            data: List[List[str]]
    ) -> Tuple[Dict[int, Tuple[int, int]], List[int], List[int]]:
        """
        Scan the galaxy to find the empty rows, columns, and stars.
        """
        next_idx = 1
        known_stars = {}
        rows_without_stars = set(range(len(data)))
        columns_without_stars = set(range(len(data[0])))

        for row_idx, data_row in enumerate(data):
            for col_idx, data_value in enumerate(data_row):
                if data_value == cls._STAR_CHAR:
                    rows_without_stars -= {row_idx}
                    columns_without_stars -= {col_idx}
                    known_stars[next_idx] = (row_idx, col_idx)
                    next_idx += 1

        return (
            known_stars,
            sorted(list(rows_without_stars)),
            sorted(list(columns_without_stars))
        )

    @classmethod
    def _shortest_paths(cls, data: List[str], factor: int) -> int:
        """
        Manhattan Distance Time!
        """
        results = 0

        known_stars, rows_without_stars, columns_without_stars = (
            cls._scan_galaxy(cls._convert_data(data))
        )

        for (x1, y1), (x2, y2) in list(combinations(known_stars.values(), 2)):
            for x in range(min(x1, x2), max(x1, x2)):
                results += factor if x in rows_without_stars else 1
            for y in range(min(y1, y2), max(y1, y2)):
                results += factor if y in columns_without_stars else 1

        return results

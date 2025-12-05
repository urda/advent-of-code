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


class Day04(DayMeta):
    """
    Advent of Code 2025, Day 04
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_04.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 04.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        can_reach = 0

        for row_idx, row in enumerate(data):
            for col_idx, col in enumerate(row):
                if col == '@':
                    if cls._fewer_four_check((row_idx, col_idx), data):
                        can_reach += 1

        return can_reach

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 04.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        can_reach = 0

        while True:
            removed_round = 0
            to_remove = []
            for row_idx, row in enumerate(data):
                for col_idx, col in enumerate(row):
                    if col == '@':
                        if cls._fewer_four_check((row_idx, col_idx), data):
                            removed_round += 1
                            to_remove.append((row_idx, col_idx))
            if removed_round == 0:
                break

            can_reach += removed_round
            for row_idx, col_idx in to_remove:
                data[row_idx] = (
                        data[row_idx][:col_idx] +
                        '.' +
                        data[row_idx][col_idx+1:]
                )

        return can_reach

    _EIGHT_WAY = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    @classmethod
    def _neighbors8(cls, grid: list[str], row: int, col: int):
        height = len(grid)
        width = len(grid[0]) if grid else 0

        for d_row, d_col in cls._EIGHT_WAY:
            neighbor_row, neighbor_col = row + d_row, col + d_col
            if 0 <= neighbor_row < height and 0 <= neighbor_col < width:
                yield neighbor_row, neighbor_col

    @classmethod
    def _fewer_four_check(cls, pos: tuple[int, int], data: list[str]) -> bool:
        target = '@'
        seen = 0
        for row, col in cls._neighbors8(data, pos[0], pos[1]):
            value = data[row][col]
            if value == target:
                seen += 1
            if seen >= 4:
                return False
        return True

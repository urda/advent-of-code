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

from typing import (
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day03(DayMeta):
    """
    Advent of Code 2023, Day 03
    """

    _gear_char = '*'
    _no_op_char = '.'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_03.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 03.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """

        result = 0
        boundaries = cls._compute_boundaries(data)

        for row_idx, row_line in enumerate(data):
            start_idx = -1
            end_idx = -1
            # what about numbers that end the line
            for column_idx, char_val in enumerate(row_line):
                if char_val.isdigit():
                    if start_idx == -1:
                        start_idx = column_idx

                    end_idx = column_idx

                if start_idx == -1:
                    continue

                if column_idx == boundaries[1] - 1 or not char_val.isdigit():
                    holding = cls._computed_part_number(
                        data,
                        row_idx,
                        start_idx,
                        end_idx,
                    )
                    result += holding

                    start_idx = end_idx = -1

        return result

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 03.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        result = 0
        boundaries = cls._compute_boundaries(data)

        reporting = {}
        for row_idx, row_line in enumerate(data):
            start_idx = -1
            end_idx = -1
            # what about numbers that end the line
            for column_idx, char_val in enumerate(row_line):
                if char_val.isdigit():
                    if start_idx == -1:
                        start_idx = column_idx

                    end_idx = column_idx

                if start_idx == -1:
                    continue

                if column_idx == boundaries[1] - 1 or not char_val.isdigit():
                    gear_points = cls._gear_points(
                        data,
                        row_idx,
                        start_idx,
                        end_idx,
                    )
                    if len(gear_points) <= 0:
                        start_idx = end_idx = -1
                        continue

                    for gear_point in gear_points:
                        curr_gear_point = reporting.get(gear_point, [])
                        curr_gear_point.append(cls._computed_part_number(
                            data,
                            row_idx,
                            start_idx,
                            end_idx,
                        ))
                        reporting[gear_point] = curr_gear_point

                    start_idx = end_idx = -1

        for gear_point, gears in reporting.items():
            if len(gears) != 2:
                continue

            result += gears[0] * gears[1]

        return result

    @classmethod
    def _compute_boundaries(cls, raw_grid: List[str]) -> tuple[int, int]:
        """
        Given an input grid, find the row and column limits.

        NOTE: This assumes a uniform grid,
              sit only checks the first row's length!
        """
        if len(raw_grid) < 1 or len(raw_grid[0]) < 1:
            raise ValueError('Invalid Grid!')

        row_count = len(raw_grid)
        column_count = len(raw_grid[0])
        return row_count, column_count

    @classmethod
    def _compute_neighbors(
            cls,
            row_idx: int,
            column_start_idx: int,
            column_end_idx: int,
            boundaries: tuple[int, int],
    ) -> list[tuple[int, int]]:
        """
        Given a row, the column start, column end, and grid boundaries:

        Find all the possible "legal" neighbor indexes.
        """

        neighbors = []

        if column_start_idx - 1 >= 0:
            # Northwest Corner
            if row_idx - 1 >= 0:
                neighbors.append((row_idx - 1, column_start_idx - 1))
            # West Neighbor
            neighbors.append((row_idx, column_start_idx - 1))
            # Southwest Corner
            if row_idx + 1 < boundaries[0]:
                neighbors.append((row_idx + 1, column_start_idx - 1))

        if column_end_idx + 1 < boundaries[1]:
            # Northeast Corner
            if row_idx - 1 >= 0:
                neighbors.append((row_idx - 1, column_end_idx + 1))
            # East Neighbor
            neighbors.append((row_idx, column_end_idx + 1))
            # Southwest Corner
            if row_idx + 1 < boundaries[0]:
                neighbors.append((row_idx + 1, column_end_idx + 1))

        for column_idx in range(column_start_idx, column_end_idx + 1):
            if row_idx - 1 >= 0:
                # Find north Neighbors (row - 1)
                neighbors.append((row_idx - 1, column_idx))

            if row_idx + 1 < boundaries[0]:
                # Find south Neighbors (row + 1)
                neighbors.append((row_idx + 1, column_idx))

        return neighbors

    @classmethod
    def _computed_part_number(
            cls,
            grid: List[str],
            row_idx: int,
            column_start_idx: int,
            column_end_idx: int,
    ) -> int:
        """
        Given a part numbers row, start, and end column, extract the integer.
        """
        has_symbol_neighbor = cls._has_symbol_neighbor(
            grid,
            row_idx,
            column_start_idx,
            column_end_idx,
        )

        if not has_symbol_neighbor:
            return 0

        return cls._extract_part_number(
            grid,
            row_idx,
            column_start_idx,
            column_end_idx,
        )

    @classmethod
    def _gear_points(
            cls,
            grid: List[str],
            row_idx: int,
            column_start_idx: int,
            column_end_idx: int,
    ) -> List[Tuple[int, int]]:
        """
        Given a row, and known start-end for a number cell, determine if any
        gear points are present and return them.
        """
        gear_points = cls._find_symbol(
            grid,
            row_idx,
            column_start_idx,
            column_end_idx,
        )
        return gear_points

    @classmethod
    def _extract_part_number(
            cls,
            grid: List[str],
            row_idx: int,
            column_start_idx: int,
            column_end_idx: int,
    ) -> int:
        """
        Pull and parse the integer from the grid at the start and end point
        in the given row.
        """
        result_str = ''
        for column_idx in range(column_start_idx, column_end_idx + 1):
            result_str += grid[row_idx][column_idx]
        result_val = int(result_str)
        return result_val

    @classmethod
    def _find_symbol(
            cls,
            grid: List[str],
            row_idx: int,
            column_start_idx: int,
            column_end_idx: int,
    ) -> List[Tuple[int, int]]:
        """
        Given a known symbol, search the neighbors and report indexes.
        """
        results = []

        boundaries = cls._compute_boundaries(grid)
        neighbors = cls._compute_neighbors(
            row_idx,
            column_start_idx,
            column_end_idx,
            boundaries,
        )

        for curr_row_idx, column_idx in neighbors:
            target = grid[curr_row_idx][column_idx]
            if target == cls._gear_char:
                results.append((curr_row_idx, column_idx))

        return results

    @classmethod
    def _has_symbol_neighbor(
            cls,
            grid: List[str],
            row_idx: int,
            column_start_idx: int,
            column_end_idx: int,
    ) -> bool:
        """
        Report if there is any symbol around the given location.
        """
        boundaries = cls._compute_boundaries(grid)
        neighbors = cls._compute_neighbors(
            row_idx,
            column_start_idx,
            column_end_idx,
            boundaries,
        )

        for curr_row_idx, column_idx in neighbors:
            target = grid[curr_row_idx][column_idx]
            if target != cls._no_op_char:
                return True

        return False

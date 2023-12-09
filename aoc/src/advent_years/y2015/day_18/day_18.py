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


class Day18(DayMeta):
    """
    Advent of Code 2015, Day 18
    """

    _grid_neighbors = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_18.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 18.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls.run_grid(data, 100, False)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 18.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls.run_grid(data, 100, True)

    @classmethod
    def run_grid(
            cls,
            raw_grid: List[str],
            rounds: int,
            lock_lights: bool
    ) -> int:
        """
        Given a raw grid input, and desired rounds, run the grid lights.
        """
        grid = cls._build_grid(raw_grid)
        boundaries = cls._get_boundaries(grid)

        if lock_lights:
            grid = cls._force_corners_on(grid)

        for _ in range(rounds):
            grid = cls._step_grid(grid, boundaries)
            if lock_lights:
                grid = cls._force_corners_on(grid)

        return cls._count_lights_on_grid(grid)

    @classmethod
    def _build_grid(cls, data: List[str]) -> List[List[bool]]:
        """
        Given the raw advent data, build the light grid as bools.b
        """
        board = []
        for row_entry in data:
            row = []
            for point in row_entry:
                row.append(point == '#')
            board.append(row)
        return board

    @classmethod
    def _count_lights_on_grid(cls, grid: List[List[bool]]) -> int:
        """
        Count the lights that are turned on, on the grid.
        """
        result = 0
        for grid_row in grid:
            result += sum(grid_row)
        return result

    @classmethod
    def _force_corners_on(cls, grid: List[List[bool]]) -> List[List[bool]]:
        """
        Force the corners of a given grid to be 'on'.
        """
        grid[0][0] = grid[0][-1] = grid[-1][0] = grid[-1][-1] = True
        return grid

    @classmethod
    def _get_boundaries(cls, grid: List[List[bool]]) -> Tuple[int, int]:
        """
        Get the (Row x Column) size of the fixed grid.
        """
        return len(grid), len(grid[0])

    @classmethod
    def _get_neighbor_idxs(
            cls,
            row: int,
            column: int,
            boundaries: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """
        Given a point on the grid and known boundaries,
        report neighbor indexes.
        """
        results = []

        for row_offset, col_offset in cls._grid_neighbors:
            target_row = row + row_offset
            target_col = column + col_offset
            if (
                    (target_row < 0 or target_row >= boundaries[0])
                    or (target_col < 0 or target_col >= boundaries[1])
            ):
                continue
            results.append((target_row, target_col))

        return results

    @classmethod
    def _get_neighbor_light_count(
            cls,
            row: int,
            column: int,
            grid: List[List[bool]],
            boundaries: Tuple[int, int]
    ) -> int:
        """
        Given a point on the grid, the grid, and known boundaries,
        count the number of lights surrounding.
        """
        search_space = cls._get_neighbor_idxs(row, column, boundaries)

        result = 0
        for row_idx, col_idx in search_space:
            state = grid[row_idx][col_idx]
            if state:
                result += 1

        return result

    @classmethod
    def _step_grid(
            cls,
            grid: List[List[bool]],
            boundaries: Tuple[int, int]
    ) -> List[List[bool]]:
        """
        Walk the entire grid, and set up the next 'step' from it.
        """
        new_grid = []
        for row_idx, grid_row in enumerate(grid):
            new_grid_row = []
            for column_idx, grid_entry in enumerate(grid_row):
                neighbor_light_count = cls._get_neighbor_light_count(
                    row_idx,
                    column_idx,
                    grid,
                    boundaries,
                )

                if grid_entry:
                    append_target = bool(neighbor_light_count in (2, 3))
                else:
                    append_target = bool(neighbor_light_count == 3)
                new_grid_row.append(append_target)
            new_grid.append(new_grid_row)
        return new_grid

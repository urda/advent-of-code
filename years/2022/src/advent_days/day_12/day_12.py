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

from queue import PriorityQueue
from typing import (
    Any,
    List,
    Set,
    Tuple,
)

from .hill_coordinate import HillCoordinate
from ..day_meta import DayMeta


class Day12(DayMeta):
    """
    Advent of Code 2022, Day 12
    """

    _pathing = [[0, -1], [0, 1], [1, 0], [-1, 0]]  # Up, Down, Left, Right

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_12.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 12.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        grid, start_coord, end_coord = cls._parse_grid(data)
        return cls._dijkstra(grid, start_coord, end_coord)

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 12.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        paths = []
        grid, start_coord, end_coord = cls._parse_grid(data)
        search_space = cls._get_all_a_starts(grid)
        search_space.append(start_coord)

        for search_coord in search_space:
            result = cls._dijkstra(grid, search_coord, end_coord)

            if result > 0:
                paths.append(result)

        return min(paths)

    @classmethod
    def _dijkstra(
            cls,
            grid: List[List[HillCoordinate]],
            start: HillCoordinate,
            target: HillCoordinate,

    ) -> int:
        idx_x_max, idx_y_max = cls._parse_grid_dimensions(grid)

        visited: Set[Tuple[int, int]] = set()
        search_space = PriorityQueue()
        search_space.put((0, start))

        while not search_space.empty():
            steps, curr_pos = search_space.get()

            if curr_pos == target:
                return steps

            if curr_pos.coords in visited:
                continue
            visited.add(curr_pos.coords)

            for direction in cls._pathing:
                new_x = curr_pos.coords[0] + direction[0]
                new_y = curr_pos.coords[1] + direction[1]

                # Boundary Check
                boundary_violation = (
                        new_x < 0 or new_x >= idx_x_max
                        or new_y < 0 or new_y >= idx_y_max
                )

                if boundary_violation:
                    continue

                next_coord = cls._get_from_grid(grid, new_x, new_y)
                if next_coord.coords in visited:
                    continue

                if not curr_pos.can_navigate_to(next_coord):
                    continue

                search_space.put((steps + 1, next_coord))

        # Failed to find a path
        return -1

    @classmethod
    def _get_all_a_starts(
            cls,
            grid: List[List[HillCoordinate]]
    ) -> List[HillCoordinate]:
        results = []
        for grid_row in grid:
            for grid_entry in grid_row:
                if grid_entry.elevation_char == 'a':
                    results.append(grid_entry)
        return results

    @classmethod
    def _get_from_grid(
            cls,
            grid: List[List[HillCoordinate]],
            x_pos: int,
            y_pos: int,
    ) -> HillCoordinate:
        return grid[y_pos][x_pos]

    @classmethod
    def _parse_grid(
            cls,
            data: List[str]
    ) -> Tuple[List[List[HillCoordinate]], HillCoordinate, HillCoordinate]:
        results = []
        start_coord = None
        end_coord = None

        for idx_y, data_line in enumerate(data):
            new_line = []
            for idx_x, data_char in enumerate(data_line):
                value = HillCoordinate(idx_x, idx_y, data_char)

                if not start_coord and value.is_start_coord:
                    start_coord = value

                if not end_coord and value.is_end_coord:
                    end_coord = value

                new_line.append(value)
            results.append(new_line)

        return results, start_coord, end_coord

    @classmethod
    def _parse_grid_dimensions(cls, grid: List[List[Any]]) -> Tuple[int, int]:
        """
        Given a parsed grid, find the WIDTH (x) and HEIGHT (y)
        :param grid: The built or raw grid to check.
        :return: The dimensions as (width x height) or (x_max by y_max)
        """
        return len(grid[0]), len(grid)

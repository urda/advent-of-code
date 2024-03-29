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

from typing import (
    List,
    Set,
    Tuple,
)

from .direction import Direction
from ..day_meta import DayMeta


class Day08(DayMeta):
    """
    Advent of Code 2022, Day 08
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_of_integer_lists('day_08.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[List[int]]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param data: The raw data from Advent of Code
        :returns: The result for Part 1
        """
        result = cls._compute_edge_count(data)
        result += cls._scope(data)
        return result

    @classmethod
    def compute_part_2(cls, data: List[List[int]]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param data: The raw data from Advent of Code
        :returns: The result for Part 2
        """
        return cls._scenic_search(data)

    @classmethod
    def _compute_edge_count(cls, parsed: List[List[int]]) -> int:
        """
        Compute the edges of the map for the "seen".

        :param parsed: The parsed tree field.
        :return: The computed seen trees at edge.
        """
        return (len(parsed[0]) * 2) + (len(parsed) * 2) - 4

    @classmethod
    def _scenic_search(cls, parsed: List[List[int]]) -> int:
        """
        Perform the search to find the best scenic spot.
        :param parsed: The parsed tree field.
        :return: The computed seen trees at edge.
        """

        row_count = len(parsed)
        column_count = len(parsed[0])
        result = -1

        search_space = [
            Direction.NORTH,
            Direction.SOUTH,
            Direction.EAST,
            Direction.WEST,
        ]

        for row_idx in range(row_count):
            for column_idx in range(column_count):
                target = (row_idx, column_idx)

                local_results = []
                for direction in search_space:
                    local_results.append(
                        cls._scenic_search_local(parsed, target, direction)
                    )
                computed = 1
                for local_result in local_results:
                    computed = computed * local_result

                if computed > result:
                    result = computed

        return result

    @classmethod
    def _scenic_search_local(
            cls,
            parsed: List[List[int]],
            idx: Tuple[int, int],
            direction: Direction,
    ) -> int:
        """
        Given the location to consider and other factors, determine the score.

        :param parsed: The parsed tree field.
        :param idx: The "idx" of interest to examine.
        :param direction: The "direction" of interest to examine.
        :return:
        """
        row_idx, column_idx = idx

        match direction:
            case Direction.NORTH:
                search_range = range(row_idx, -1, -1)
            case Direction.SOUTH:
                search_range = range(row_idx, len(parsed), 1)
            case Direction.EAST:
                search_range = range(column_idx, len(parsed[0]), 1)
            case Direction.WEST:
                search_range = range(column_idx, -1, -1)
            case _:
                raise NotImplementedError

        match direction:
            case Direction.NORTH | Direction.SOUTH:
                locked_value = column_idx
            case Direction.EAST | Direction.WEST:
                locked_value = row_idx
            case _:
                raise NotImplementedError

        max_height = None
        results = 0
        for search_idx in search_range:
            if direction in (Direction.NORTH, Direction.SOUTH):
                looking_at_tree = parsed[search_idx][locked_value]
            else:
                looking_at_tree = parsed[locked_value][search_idx]

            if not max_height:
                max_height = looking_at_tree
                continue

            results += 1
            if looking_at_tree >= max_height:
                break

        return results

    @classmethod
    def _scope(cls, parsed: List[List[int]]) -> int:
        """Scope the interior of the tree field."""
        results = set()

        for row_idx in range(1, len(parsed) - 1):
            for direction in (Direction.EAST, Direction.WEST):
                results.update(
                    cls._parse_row(parsed, row_idx, direction)
                )

        for column_idx in range(1, len(parsed[0]) - 1):
            for direction in (Direction.NORTH, Direction.SOUTH):
                results.update(
                    cls._parse_column(parsed, column_idx, direction)
                )

        return len(results)

    @classmethod
    def _parse_column(
            cls,
            data: List[List[int]],
            column_idx: int,
            direction: Direction,
    ) -> Set[Tuple[int, int]]:
        """
        Parse a given column for trees
        :param data: The parsed tree field.
        :param column_idx: The column's index we're looking at.
        :param direction: The direction to search in the column.
        :return: A set of coordinates of seen result trees.
        """
        match direction:
            case Direction.SOUTH:
                step = 1
                tree_pov = data[0][column_idx]
            case Direction.NORTH:
                step = -1
                data_height = len(data) - 1
                tree_pov = data[data_height][column_idx]
            case _:
                raise NotImplementedError

        min_height = tree_pov
        row_range = range(0, len(data)) if step > 0 \
            else range(len(data) - 1, -1, -1)

        results = set()

        for row_idx in row_range:
            if row_idx in (0, len(data) - 1):
                continue

            looking_at_tree = data[row_idx][column_idx]
            if looking_at_tree > min_height:
                results.add((row_idx, column_idx))
                min_height = looking_at_tree

        return results

    @classmethod
    def _parse_row(
            cls,
            data: List[List[int]],
            row_idx: int,
            direction: Direction,
    ) -> Set[Tuple[int, int]]:
        """
        Parse a given row for trees.
        :param data: The parsed tree field.
        :param row_idx: The row's index we're looking at.
        :param direction: The direction to search in the row.
        :return: A set of coordinates of seen result trees.
        """
        row = data[row_idx]

        match direction:
            case Direction.EAST:
                step = 1
                tree_pov = row[0]
            case Direction.WEST:
                step = -1
                tree_pov = row[-1]
            case _:
                raise NotImplementedError

        min_height = tree_pov

        results = set()
        for column_idx, _ in enumerate(row[::step]):
            column_idx_actual = column_idx if step > 0 \
                else len(row) - 1 - column_idx

            if column_idx_actual in (0, len(row) - 1):
                continue

            looking_at_tree = data[row_idx][column_idx_actual]
            if looking_at_tree > min_height:
                results.add((row_idx, column_idx_actual))
                min_height = looking_at_tree

        return results

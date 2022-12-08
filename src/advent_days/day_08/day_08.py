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

from enum import Enum
from typing import (
    List,
    Set,
    Tuple,
)

from ..day_meta import DayMeta


class ScopeMode(Enum):
    Column = 1
    Row = 2


class Direction(Enum):
    North = 1
    South = 2
    East = 3
    West = 4


class Day08(DayMeta):
    """
    Advent of Code 2022, Day 08
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_08.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        tree_grid = cls._parse_data(data)

        result = cls._compute_edge_count(tree_grid)
        result += cls._scope(tree_grid)

        return result

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        tree_grid = cls._parse_data(data)
        return cls._scenic_search(tree_grid)

    @classmethod
    def _compute_edge_count(cls, parsed: List[List[int]]) -> int:
        return (len(parsed[0]) * 2) + (len(parsed) * 2) - 4

    @classmethod
    def _scenic_search(cls, parsed: List[List[int]]) -> int:
        row_count = len(parsed)
        column_count = len(parsed[0])
        result = -1

        for row_idx in range(row_count):
            for column_idx in range(column_count):
                target = (row_idx, column_idx)
                north = cls._scenic_search_local(parsed, target, Direction.North)
                south = cls._scenic_search_local(parsed, target, Direction.South)
                east = cls._scenic_search_local(parsed, target, Direction.East)
                west = cls._scenic_search_local(parsed, target, Direction.West)

                local_result = north * south * east * west

                if local_result > result:
                    result = local_result

        return result

    @classmethod
    def _scenic_search_local(
            cls,
            parsed: List[List[int]],
            idx: Tuple[int, int],
            direction: Direction,
    ) -> int:
        row_idx, column_idx = idx

        match direction:
            case Direction.North:
                search_range = range(row_idx, -1, -1)
                locked_value = column_idx
            case Direction.South:
                search_range = range(row_idx, len(parsed), 1)
                locked_value = column_idx
            case Direction.East:
                search_range = range(column_idx, len(parsed[0]), 1)
                locked_value = row_idx
            case Direction.West:
                search_range = range(column_idx, -1, -1)
                locked_value = row_idx
            case _:
                raise NotImplementedError

        max_height = None
        results = 0
        if direction in (Direction.North, Direction.South):
            for search_idx in search_range:
                looking_at_tree = parsed[search_idx][locked_value]

                if not max_height:
                    max_height = looking_at_tree
                    continue

                results += 1
                if looking_at_tree >= max_height:
                    break
        else:
            for search_idx in search_range:
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
        results = set()

        for row_idx in range(1, len(parsed) - 1):
            east = cls._parse_row(parsed, row_idx, Direction.East)
            west = cls._parse_row(parsed, row_idx, Direction.West)
            results.update(east)
            results.update(west)

        for column_idx in range(1, len(parsed[0]) - 1):
            north = cls._parse_column(parsed, column_idx, Direction.North)
            south = cls._parse_column(parsed, column_idx, Direction.South)
            results.update(north)
            results.update(south)

        return len(results)

    @classmethod
    def _parse_column(
            cls,
            data: List[List[int]],
            column_idx: int,
            direction: Direction,
    ) -> Set[Tuple[int, int]]:
        match direction:
            case Direction.South:
                step = 1
                tree_pov = data[0][column_idx]
            case Direction.North:
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
            if row_idx in (0, len(data) -1):
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
        row = data[row_idx]

        match direction:
            case Direction.East:
                step = 1
                tree_pov = row[0]
            case Direction.West:
                step = -1
                tree_pov = row[-1]
            case _:
                raise NotImplementedError

        min_height = tree_pov

        results = set()
        for column_idx, tree in enumerate(row[::step]):
            column_idx_actual = column_idx if step > 0 \
                else len(row) - 1 - column_idx

            if column_idx_actual in (0, len(row) - 1):
                continue

            looking_at_tree = data[row_idx][column_idx_actual]
            if looking_at_tree > min_height:
                results.add((row_idx, column_idx_actual))
                min_height = looking_at_tree

        return results

    @classmethod
    def _parse_data(cls, data: List[str]) -> List[List[int]]:
        rows = []
        for raw_data in data:
            curr_row = []
            for entry in raw_data:
                curr_row.append(int(entry))
            rows.append(curr_row)
        return rows

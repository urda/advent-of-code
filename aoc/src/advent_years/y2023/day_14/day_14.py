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


class Day14(DayMeta):
    """
    Advent of Code 2023, Day 14
    """

    _NORTH = (-1, 0)
    _SOUTH = (1, 0)
    _EAST = (0, 1)
    _WEST = (0, -1)

    _CYCLE_STEPS = [
        _NORTH,
        _WEST,
        _SOUTH,
        _EAST,
    ]

    _EMPTY_SPACE = '.'
    _ROCK_CUBE = '#'
    _ROCK_ROUND = 'O'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_14.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 14.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        data = cls._tilts_rocks(data, cls._NORTH)
        return cls._get_load(data, cls._NORTH)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 14.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._tilt_cycles(data)

    @classmethod
    def _tilt_cycles(
            cls,
            data: List[str],
    ) -> int:
        history = {}
        history_jump = []
        loop_start = None
        loop_size = None

        for cycle_idx in range(1_000_000_000):
            for tilt_dir in cls._CYCLE_STEPS:
                data = cls._tilts_rocks(data, tilt_dir)

            temp_rocks = frozenset(data)
            prev_rocks = frozenset((tuple(temp_rocks),))

            if prev_rocks in history:
                loop_start = history[prev_rocks]
                loop_size = cycle_idx - loop_start
                break
            history[prev_rocks] = cycle_idx
            history_jump.append(cls._get_load(data, cls._NORTH))

        target = loop_start + (999_999_999 - loop_start) % loop_size

        return history_jump[target]

    # noinspection DuplicatedCode
    @classmethod
    def _tilts_rocks(
            cls,
            data: List[str],
            tilt_direction: Tuple[int, int],
    ) -> List[str]:
        fixed = (cls._EMPTY_SPACE, cls._ROCK_CUBE)

        is_col_scan = tilt_direction in (cls._NORTH, cls._SOUTH)

        if is_col_scan:
            for col_idx in range(len(data[0])):
                scanner = range(len(data))
                if tilt_direction == cls._SOUTH:
                    scanner = reversed(scanner)

                for row_idx in scanner:
                    if data[row_idx][col_idx] in fixed:
                        continue
                    data = cls._tilt_rock(
                        data, (row_idx, col_idx), tilt_direction
                    )
        else:
            for row_idx, row_data in enumerate(data):
                scanner = range(len(row_data))
                if tilt_direction == cls._EAST:
                    scanner = reversed(scanner)

                for col_idx in scanner:
                    if row_data[col_idx] in fixed:
                        continue
                    data = cls._tilt_rock(
                        data, (row_idx, col_idx), tilt_direction
                    )

        return data

    @classmethod
    def _get_load(
            cls,
            data: List[str],
            tilt_direction: Tuple[int, int],
    ) -> int:
        results = 0
        match tilt_direction:
            case cls._NORTH:
                mul_factor = len(data)
                mul_redux = -1
                for _, data_row in enumerate(data):
                    results += (mul_factor * data_row.count(cls._ROCK_ROUND))
                    mul_factor = mul_factor + mul_redux
            case _:
                raise ValueError

        return results

    @classmethod
    def _tilt_rock(
            cls,
            data: List[str],
            start_pos: Tuple[int, int],
            tilt_direction: Tuple[int, int],
    ) -> List[str]:
        row_limit = len(data)
        col_limit = len(data[0])

        last_free = start_pos
        while True:
            next_val = (
                last_free[0] + tilt_direction[0],
                last_free[1] + tilt_direction[1]
            )
            if (next_val[0] < 0) or (next_val[0] >= row_limit):
                break
            if (next_val[1] < 0) or (next_val[1] >= col_limit):
                break
            data_row = list(data[next_val[0]])
            next_char = data_row[next_val[1]]
            if next_char in (cls._ROCK_CUBE, cls._ROCK_ROUND):
                break
            last_free = next_val

        if start_pos == last_free:
            return data

        old_row = list(data[start_pos[0]])
        old_row[start_pos[1]] = cls._EMPTY_SPACE
        data[start_pos[0]] = ''.join(old_row)
        fix_row = list(data[last_free[0]])
        fix_row[last_free[1]] = cls._ROCK_ROUND
        data[last_free[0]] = ''.join(fix_row)

        return data

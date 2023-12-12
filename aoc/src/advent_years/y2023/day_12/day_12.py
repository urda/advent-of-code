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

import functools
from typing import (
    List,
    Optional,
    Tuple,
)

from ..day_meta import DayMeta


class Day12(DayMeta):
    """
    Advent of Code 2023, Day 12
    """

    _OPERATIONAL = '.'
    _DAMAGED = '#'
    _UNKNOWN = '?'

    _FOLD_SIZE = 5

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
        return cls._solver(data, False)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 12.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._solver(data, True)

    @classmethod
    def _parse_data_line(cls, data_line: str) -> Tuple[str, Tuple[int]]:
        raw_reports, raw_group_sizes = data_line.split(' ')
        group_sizes = [int(x) for x in raw_group_sizes.split(',')]
        return raw_reports, tuple(group_sizes)

    @classmethod
    @functools.lru_cache(maxsize=None)
    def _solve(
            cls,
            data: str,
            inner_run: Optional[int],
            groups: Tuple[int, ...]
    ):
        if not data:
            if (
                    (inner_run is None and len(groups) == 0)
                    or
                    (len(groups) == 1 and inner_run is not None
                     and inner_run == groups[0])
            ):
                return 1
            return 0
        possibles = 0
        possible_value = (cls._DAMAGED, cls._UNKNOWN)
        for char_val in data:
            if char_val in possible_value:
                possibles += 1

        poss = 0
        target = data[0]

        # pylint: disable=too-many-boolean-expressions
        if (
            (inner_run is not None and possibles + inner_run < sum(groups))
            or (inner_run is None and possibles < sum(groups))
            or (inner_run is not None and len(groups) == 0)
            or (
                target == cls._OPERATIONAL
                and inner_run is not None
                and inner_run != groups[0]
            )
        ):
            return 0

        if (
                (target == cls._OPERATIONAL and inner_run is not None)
                or
                (target == cls._UNKNOWN and inner_run is not None
                 and inner_run == groups[0])
        ):
            poss += cls._solve(data[1:], None, groups[1:])

        if (target in (cls._DAMAGED, cls._UNKNOWN)) and inner_run is not None:
            poss += cls._solve(data[1:], inner_run + 1, groups)

        if (target in (cls._DAMAGED, cls._UNKNOWN)) and inner_run is None:
            poss += cls._solve(data[1:], 1, groups)

        if (target in (cls._OPERATIONAL, cls._UNKNOWN)) and inner_run is None:
            poss += cls._solve(data[1:], None, groups)

        return poss

    @classmethod
    def _solver(cls, data: List[str], folded_mode: bool):
        """
        The solver can handle either non-folded-mode (part 1)
        and folded-mode (part 2).
        """
        results = 0
        for data_line in data:
            raw_reports, group_sizes = cls._parse_data_line(data_line)
            if folded_mode:
                target = ''
                for _ in range(cls._FOLD_SIZE):
                    target += f'?{raw_reports}'
                target = target[1:]
                target_groups = group_sizes * cls._FOLD_SIZE
            else:
                target = raw_reports
                target_groups = group_sizes

            results += cls._solve(target, None, target_groups)
        return results

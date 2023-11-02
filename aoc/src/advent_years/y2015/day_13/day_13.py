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

import itertools
from typing import (
    Dict,
    List,
    Tuple,
)

from .knight import Knight
from ..day_meta import DayMeta


class Day13(DayMeta):
    """
    Advent of Code 2015, Day 13
    """

    # pylint: disable=duplicate-code
    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_13.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    # pylint: disable=duplicate-code
    @classmethod
    def compute_part_1(cls, data) -> int:
        """
        Parse the data and compute for Day 13.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        knights: Dict[str, Knight] = cls._parse(data)
        return cls._compute_part(knights)

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 13.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        knights: Dict[str, Knight] = cls._parse(data)
        cls._build_and_add_self(knights)
        return cls._compute_part(knights)

    @classmethod
    def _compute_part(cls, knights: Dict[str, Knight]) -> int:
        knight_names: List[str] = list(knights.keys())

        best_result = int(-10e10)
        knight_group: Tuple[str, ...]
        for knight_group in itertools.permutations(knight_names):
            local_result = cls._build_happy_ring(knight_group, knights)

            if local_result > best_result:
                best_result = local_result

        return best_result

    @classmethod
    def _build_and_add_self(cls, knight_pool: Dict[str, Knight]) -> None:
        knight = Knight('Self')

        for knight_name in knight_pool.keys():
            knight.register_relation(knight_name, 0)
            knight_pool[knight_name].register_relation('Self', 0)

        knight_pool[knight.name] = knight

    @classmethod
    def _build_happy_ring(
            cls,
            knight_order: Tuple[str, ...],
            knight_pool: Dict[str, Knight]
    ) -> int:
        knight_max_idx = len(knight_order) - 1

        results = 0
        for idx, knight_name in enumerate(knight_order):
            curr_knight = knight_pool[knight_name]

            neighbor_left = idx - 1
            neighbor_right = idx + 1
            if idx == 0:
                neighbor_left = len(knight_order) - 1
            elif idx == knight_max_idx:
                neighbor_right = 0

            target_left = knight_order[neighbor_left]
            target_right = knight_order[neighbor_right]

            happy_left = curr_knight.get_relation(target_left)
            happy_right = curr_knight.get_relation(target_right)

            results += happy_left + happy_right

        return results

    @classmethod
    def determine_polarity(cls, polarity_value: str) -> int:
        """From the text, determine a value's polarity."""
        match polarity_value.lower():
            case 'gain':
                return 1
            case 'lose':
                return -1
            case _:
                raise ValueError(f"Unrecognized token '{polarity_value}'")

    @classmethod
    def _parse(cls, data: str) -> Dict[str, Knight]:
        results = {}
        for entry in data:
            tokens = entry.split(' ')
            curr_knight = tokens[0]
            curr_sign = cls.determine_polarity(tokens[2])
            curr_value = int(tokens[3]) * curr_sign
            curr_target = tokens[-1][:-1]

            if curr_knight not in results:
                results[curr_knight] = Knight(curr_knight)
            knight = results[curr_knight]

            knight.register_relation(curr_target, curr_value)

        return results

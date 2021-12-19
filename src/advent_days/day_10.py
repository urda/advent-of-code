"""
Copyright 2021 Peter Urda

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

import copy
from enum import Enum
from typing import (
    List,
    Tuple,
)

from advent_days.day_meta import DayMeta


class ParseMode(Enum):
    """
    Enum to control parse mode
    """
    CORRUPTED = 'CORRUPTED'
    INCOMPLETE = 'INCOMPLETE'


class Day10(DayMeta):
    """
    Advent Day 10
    """

    _data_file = 'day_10.txt'

    _open_bracket = '['
    _open_carrot = '<'
    _open_curly = '{'
    _open_paren = '('

    _close_bracket = ']'
    _close_carrot = '>'
    _close_curly = '}'
    _close_paren = ')'

    _open_to_close_map = {
        _open_bracket: _close_bracket,
        _open_carrot: _close_carrot,
        _open_curly: _close_curly,
        _open_paren: _close_paren,
    }

    _close_points = {
        _close_bracket: 57,
        _close_carrot: 25137,
        _close_curly: 1197,
        _close_paren: 3,
    }

    _complete_points = {
        _close_bracket: 2,
        _close_carrot: 4,
        _close_curly: 3,
        _close_paren: 1,
    }

    _close_chars = {_close_bracket, _close_carrot, _close_curly, _close_paren}
    _open_chars = {_open_bracket, _open_carrot, _open_curly, _open_paren}
    _all_chars = _close_chars.union(_open_chars)

    @classmethod
    def compute_incomplete_stack(cls, remaining_stack: List[str]) -> int:
        """
        Compute the remaining values needed for the stack, and score it.

        :param remaining_stack: The leftover open stack values.
        :return: The score of the parse result of the incomplete line.
        """
        result = 0
        internal_stack = copy.deepcopy(remaining_stack)

        while len(internal_stack) > 0:
            character = internal_stack.pop()
            result = result * 5
            result += cls._complete_points[cls._open_to_close_map[character]]

        return result

    @classmethod
    def parse_syntax(cls, nav_data: List[str], parse_mode: ParseMode) -> int:
        """
        Parse the syntax of the nav data input.

        :param nav_data: The full list of strings of nav data.
        :param parse_mode: The parsing mode to process the nav data in.
        :return: The "score" of the syntax parse result.
        """

        result = 0
        incomplete = []
        for nav_data_entry in nav_data:
            corrupted_count, counters = \
                cls.parse_corrupted_lines(nav_data_entry)

            match parse_mode:
                case ParseMode.CORRUPTED:
                    result += corrupted_count
                case ParseMode.INCOMPLETE:
                    if corrupted_count == 0:
                        incomplete.append(counters)

        if parse_mode is ParseMode.INCOMPLETE:
            results = []

            for entry in incomplete:
                results.append(cls.compute_incomplete_stack(entry))

            results.sort()
            result = results[len(results) // 2]

        return result

    @classmethod
    def parse_corrupted_lines(
            cls,
            nav_data_line: str
    ) -> Tuple[int, List[str]]:
        """
        Parse the syntax of a single line of nav data input.

        :param nav_data_line: The singular line of nav data.
        :return: A tuple of the corrupted score, and incomplete trackers.
        """

        nav_data_chars = [*nav_data_line]

        nav_tracker = {
            cls._open_bracket: 0,
            cls._open_carrot: 0,
            cls._open_curly: 0,
            cls._open_paren: 0,
        }

        open_stack = []
        for character in nav_data_chars:
            if character not in cls._all_chars:
                raise ValueError('Unknown character in input')

            if character in cls._open_chars:
                nav_tracker[character] += 1
                open_stack.append(character)
            else:
                last_open = open_stack.pop()
                if character == cls._open_to_close_map[last_open]:
                    nav_tracker[last_open] -= 1
                else:
                    return cls._close_points[character], open_stack

        return 0, open_stack

    @classmethod
    def solve_day(cls) -> List[str]:
        nav_data = cls.get_lines_as_list_string(cls._data_file)
        part_1_result = cls.parse_syntax(nav_data, ParseMode.CORRUPTED)
        part_2_result = cls.parse_syntax(nav_data, ParseMode.INCOMPLETE)

        return [
            'Part 1:',
            f'Determined: {part_1_result}',
            '---',
            'Part 2',
            f'Determined: {part_2_result}',
        ]

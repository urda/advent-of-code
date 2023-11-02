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

from typing import (
    List,
    Tuple,
)

from .game_board import GameBoard
from ..day_meta import DayMeta


class Day04(DayMeta):
    """
    Advent Day 04
    """

    _board_fixed_column_count = 15
    _board_fixed_row_count = 5
    _data_file = 'day_04.txt'
    _header_delimiter = ','

    _failure_exception: ValueError = \
        ValueError('Unable to find a winning board, something is wrong.')

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_sum, part_1_drawn = cls.perform_part_1(cls._get_boards(),
                                                      cls._get_draw_order())
        part_2_sum, part_2_drawn = cls.perform_part_2(cls._get_boards(),
                                                      cls._get_draw_order())

        return [
            'Part 1:',
            f'Determined Unmarked Sum: {part_1_sum}',
            f'Determined Last Drawn Number: {part_1_drawn}',
            f'Determined: {part_1_sum * part_1_drawn}',
            '---',
            'Part 2:',
            f'Determined Unmarked Sum: {part_2_sum}',
            f'Determined Last Drawn Number: {part_2_drawn}',
            f'Determined: {part_2_sum * part_2_drawn}',
        ]

    @classmethod
    def _get_boards(cls) -> list[GameBoard]:
        results = []

        # pylint: disable=duplicate-code
        with open(
                cls.build_data_file_path(cls._data_file),
                'r',
                encoding='utf-8',
        ) as data_file:
            new_board_rows = []
            for line in data_file:
                # Skip any lines that do not look like board lines
                if len(line) != cls._board_fixed_column_count:
                    continue

                # Slice new line character on data line, split, convert to int
                new_board_rows.append([int(x) for x in line[:-1].split()])

                # We can create a board now
                if len(new_board_rows) == cls._board_fixed_row_count:
                    results.append(GameBoard(new_board_rows))
                    new_board_rows = []

        return results

    @classmethod
    def _get_draw_order(cls) -> List[int]:
        with open(
                cls.build_data_file_path(cls._data_file),
                'r',
                encoding='utf-8',
        ) as data_file:
            str_data = data_file.readline().split(cls._header_delimiter)
            return [int(x) for x in str_data]

    @classmethod
    def perform_part_1(
            cls,
            boards: List[GameBoard],
            draw_order: List[int],
    ) -> Tuple[int, int]:
        """
        Compute the answer to part 1 for Day 04.

        :param boards: The boards to process for this portion.
        :param draw_order: The draw order running against the boards.
        :return: Tuple of (unmarked sum, value drawn) for winner.
        """
        for value_to_report in draw_order:
            for board in boards:
                possible_result = board.report_drawn_value(value_to_report)

                if possible_result:
                    return possible_result

        raise cls._failure_exception

    @classmethod
    def perform_part_2(
            cls,
            boards: List[GameBoard],
            draw_order: List[int],
    ) -> Tuple[int, int]:
        """
        Compute the answer to part 2 for Day 04.

        :param boards: The boards to process for this portion.
        :param draw_order: The draw order running against the boards.
        :return: Tuple of (unmarked sum, value drawn) for the squid winner.
        """
        finished_board_indexes = set()
        last_seen_board = None
        last_seen_result = None

        for value_to_report in draw_order:
            for board_idx, board in enumerate(boards):
                if board_idx in finished_board_indexes:
                    continue

                possible_result = board.report_drawn_value(value_to_report)

                if possible_result:
                    last_seen_board = board
                    last_seen_result = possible_result
                    finished_board_indexes.add(board_idx)

        if not last_seen_board:
            raise cls._failure_exception

        return last_seen_result

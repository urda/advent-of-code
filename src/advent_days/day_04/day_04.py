from typing import (
    List,
    Tuple,
)

from .game_board import GameBoard
from ..day_meta import DayMeta


class Day04(DayMeta):
    _board_fixed_column_count = 15
    _board_fixed_row_count = 5
    _data_file = 'day_04.txt'
    _header_delimiter = ','

    _failure_exception = \
        ValueError('Unable to find a winning board, something is wrong.')

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_sum, part_1_drawn = cls._perform_part_1()
        part_2_sum, part_2_drawn = cls._perform_part_2()

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

        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
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
        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
            str_data = data_file.readline().split(cls._header_delimiter)
            return [int(x) for x in str_data]

    @classmethod
    def _perform_part_1(cls) -> Tuple[int, int]:
        boards = cls._get_boards()
        draw_order = cls._get_draw_order()

        for value_to_report in draw_order:
            for board in boards:
                possible_result = board.report_drawn_value(value_to_report)

                if possible_result:
                    return possible_result

        raise cls._failure_exception

    @classmethod
    def _perform_part_2(cls) -> Tuple[int, int]:
        boards = cls._get_boards()
        draw_order = cls._get_draw_order()
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

        if last_seen_board:
            return last_seen_result
        else:
            raise cls._failure_exception
from typing import List

from .day_meta import DayMeta


class Day04(DayMeta):
    _board_fixed_column_count = 15
    _board_fixed_row_count = 5
    _data_file = 'day_04.txt'
    _data_file_header_row_count = 2

    @classmethod
    def solve_day(cls) -> List[str]:
        boards = cls._get_boards()
        draw_order = cls._get_draw_order()
        return []

    @classmethod
    def _get_boards(cls) -> List[List[str]]:
        results = []

        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
            # Skip leading lines of non-board data
            for _ in range(cls._data_file_header_row_count):
                next(data_file)

            new_board_rows = []
            for line in data_file:
                if len(line) != cls._board_fixed_column_count:
                    continue

                # Slice new line character on data line
                new_board_rows.append(line[:-1])

                if len(new_board_rows) == cls._board_fixed_row_count:
                    results.append(new_board_rows)
                    new_board_rows = []

        return results

    @classmethod
    def _get_draw_order(cls) -> str:
        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
            return data_file.readline()

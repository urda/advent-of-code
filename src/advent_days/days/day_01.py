import sys
from typing import List

from .day_meta import DayMeta


class Day01(DayMeta):
    _data_file = 'day_01_data.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        return [
            f'Part 01 Determined: {cls._perform_part_1()}',
            f'Part 02 Determined: {cls._perform_part_2()}',
        ]

    @classmethod
    def _get_lines(cls) -> List[int]:
        lines = []
        with open(cls.data_dir_path(cls._data_file), 'r') as data_file:
            for line in data_file:
                try:
                    lines.append(int(line))
                except ValueError as error:
                    raise error
        return lines

    @classmethod
    def _perform_part_1(cls) -> int:
        lines = cls._get_lines()

        # Set the first seen value to the smallest value possible for
        # this system, then set counter to -1 so first value sets counter to 0
        increased_count = -1
        previous_value = ~sys.maxsize

        for current_value in lines:
            if current_value > previous_value:
                increased_count += 1
            previous_value = current_value

        return increased_count

    @classmethod
    def _perform_part_2(cls) -> int:
        lines = cls._get_lines()

        rolling_window_size = 3
        rolling_window = []
        increased_count = -1
        previous_value = ~sys.maxsize

        for loading_value in lines:
            rolling_window.append(loading_value)

            # If we don't have three entries to read, keep loading
            if len(rolling_window) < rolling_window_size:
                continue

            current_total = sum(rolling_window)

            if current_total > previous_value:
                increased_count += 1

            previous_value = current_total
            rolling_window.pop(0)

        return increased_count

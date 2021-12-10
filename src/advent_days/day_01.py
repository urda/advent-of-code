import sys
from typing import List

from .day_meta import DayMeta


class Day01(DayMeta):
    _data_file = 'day_01.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_answer = cls.compute_part_1(cls._get_lines())
        part_2_answer = cls.compute_part_2(cls._get_lines())

        return [
            f'Part 01 Determined: {part_1_answer}',
            f'Part 02 Determined: {part_2_answer}',
        ]

    @classmethod
    def _get_lines(cls) -> List[int]:
        lines = []
        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
            for line in data_file:
                try:
                    lines.append(int(line))
                except ValueError as error:
                    raise error
        return lines

    @classmethod
    def compute_part_1(cls, lines: List[int]) -> int:
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
    def compute_part_2(cls, lines: List[int]) -> int:
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

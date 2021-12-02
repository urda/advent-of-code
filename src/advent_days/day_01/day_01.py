import sys
from pathlib import Path
from typing import List


class Day01:
    _working_dir = Path(__file__).resolve().parent

    _data_file = 'day_01_data.txt'
    _data_file_path = Path(_working_dir, _data_file)

    @classmethod
    def measure_depth(cls):
        lines = cls._get_lines()

        # Set the first seen value to the smallest value possible for
        # this system, then set counter to -1 so first value sets counter to 0
        increased_count = -1
        previous_value = ~sys.maxsize

        for current_value in lines:
            if current_value > previous_value:
                increased_count += 1
            previous_value = current_value

        print(f'Determined: {increased_count}')

    @classmethod
    def _get_lines(cls) -> List[int]:
        lines = []
        with open(cls._data_file_path, 'r') as data_file:
            for line in data_file:
                try:
                    lines.append(int(line))
                except ValueError as error:
                    raise error
        return lines

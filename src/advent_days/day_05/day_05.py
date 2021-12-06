from typing import List

from .vent_map import VentMap
from ..day_meta import DayMeta


class Day05(DayMeta):
    _data_file = 'day_05.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        return []

    @classmethod
    def _get_lines(cls) -> List[str]:
        lines = []
        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
            for line in data_file:
                lines.append(line)
        return lines

    @classmethod
    def _perform_part_1(cls):
        vent_map = VentMap(cls._get_lines())

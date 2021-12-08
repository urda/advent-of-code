import sys
from collections import Counter
from typing import List

from .day_meta import DayMeta


class Day07(DayMeta):
    _data_file = 'day_07.txt'

    _data_delimiter = ','

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_crabs = cls._get_raw_data()
        raw_crab_sorted = sorted(raw_crabs)
        min_value = raw_crab_sorted[0]
        max_value = raw_crab_sorted[-1]

        crab_counter = Counter(cls._get_raw_data())

        min_fuel_seen = sys.maxsize
        alignment_result = None

        for x in range(min_value, max_value + 1):
            total_fuel_spent = 0
            for crabs in crab_counter.items():
                fuel_spent = abs(crabs[0] - x)
                fuel_spent_for_all = fuel_spent * crabs[1]
                total_fuel_spent += fuel_spent_for_all

            if total_fuel_spent < min_fuel_seen:
                min_fuel_seen = total_fuel_spent
                alignment_result = (total_fuel_spent, x)

        return [
            'Part 1:',
            f'Determined: {alignment_result[0]}',
        ]

    @classmethod
    def _get_raw_data(cls) -> List[int]:
        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
            raw_data_line = data_file.readline().strip()

        return [int(x) for x in raw_data_line.split(cls._data_delimiter)]

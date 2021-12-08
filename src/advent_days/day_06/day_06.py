from typing import List

from .laternfish import Lanternfish
from ..day_meta import DayMeta


class Day06(DayMeta):
    _data_file = 'day_06.txt'

    _data_delimiter = ','

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_result = cls._perform_part_1()
        part_2_result = cls._perform_part_2()

        return [
            'Part 1:',
            f'Determined: {part_1_result}',
            '---',
            'Part 2:',
            f'Determined: {part_2_result}',
        ]

    @classmethod
    def _get_raw_data(cls) -> List[Lanternfish]:
        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
            raw_data_line = data_file.readline().strip()

        return [
            Lanternfish(int(x)) for x in
            raw_data_line.split(cls._data_delimiter)
        ]

    @classmethod
    def _perform_part_1(cls) -> int:
        return cls._perform_work(80)

    @classmethod
    def _perform_part_2(cls) -> int:
        return cls._perform_work(256)

    @classmethod
    def _perform_work(cls, day_limit: int) -> int:
        fish_data = cls._get_raw_data()

        for _ in range(day_limit):
            new_fish_for_day = 0
            for fish in fish_data:
                should_add_fish = fish.perform_day()

                if should_add_fish:
                    new_fish_for_day += 1

            if new_fish_for_day > 0:
                for _ in range(new_fish_for_day):
                    fish_data.append(Lanternfish(8))

        return len(fish_data)

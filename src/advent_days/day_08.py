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

from collections import Counter
from typing import (
    List,
    Tuple,
)

from .day_meta import DayMeta


class Day08(DayMeta):
    """
    Advent Day 08
    """

    _data_file = 'day_08.txt'

    _data_delimiter = '|'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls._get_raw_data()
        split_raw_data = cls._split_raw_data(raw_data)

        part_1_result = cls._perform_part_1(split_raw_data)

        return [
            'Part 1:',
            f'Determined: {part_1_result}',
        ]

    @classmethod
    def _count_part_1_values(cls, output_values: List[str]) -> Counter:
        results = []
        for output_value in output_values:
            results.append(len(set(output_value)))
        return Counter(results)

    @classmethod
    def _get_raw_data(cls) -> List[str]:
        with open(
                cls.build_data_file_path(cls._data_file),
                'r',
                encoding='utf-8',
        ) as data_file:
            return data_file.readlines()

    @classmethod
    def _perform_part_1(cls, split_raw_data: List[Tuple[str, str]]) -> int:
        output_counter = Counter([])
        for _, output_digits in split_raw_data:
            output_counter += cls._count_part_1_values(output_digits.split())
        output_results = dict(output_counter.items())

        # 1: 2 Segments, 4: 4 Segments, 7: 3 Segments, 8: 7 Segments
        return \
            output_results[2] + output_results[3] + \
            output_results[4] + output_results[7]

    @classmethod
    def _split_raw_data(cls, raw_data: List[str]) -> List[Tuple[str, str]]:
        results = []
        for raw_entry in raw_data:
            split_values = raw_entry.split(cls._data_delimiter)
            results.append((split_values[0].strip(), split_values[1].strip()))
        return results

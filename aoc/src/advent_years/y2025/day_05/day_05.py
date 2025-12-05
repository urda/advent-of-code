"""
Copyright 2025 Peter Urda

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

from typing import List

from ..day_meta import DayMeta


class Day05(DayMeta):
    """
    Advent of Code 2025, Day 05
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_05.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 05.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        raw_ranges, raw_ingredients = cls._split_database(data)
        ranges = cls._raw_ranges_to_ranges(raw_ranges)
        merged_ranges = cls._merge_intervals(ranges)
        ingredients = cls._raw_ingredients_to_ingredients(raw_ingredients)

        fresh_count = 0
        for ingredient in ingredients:
            for low, high in merged_ranges:
                if low <= ingredient <= high:
                    fresh_count += 1

        return fresh_count

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 05.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        raw_ranges, _ = cls._split_database(data)
        ranges = cls._raw_ranges_to_ranges(raw_ranges)
        merged_ranges = cls._merge_intervals(ranges)

        fresh_count = 0

        for low, high in merged_ranges:
            fresh_count += high - low + 1

        return fresh_count

    @staticmethod
    def _split_database(data: list[str]) -> tuple[list[str], list[str]]:
        try:
            idx = data.index('')
        except ValueError as err:
            raise RuntimeError('Malformed AOC data.') from err
        return data[:idx], data[idx + 1:]

    @staticmethod
    def _merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
        results = []

        for low, high in sorted(intervals):
            if not results or low > results[-1][1] + 1:
                results.append([low, high])
            else:
                results[-1][1] = max(results[-1][1], high)

        return results

    @staticmethod
    def _raw_ingredients_to_ingredients(
            raw_ingredients: list[str]
    ) -> list[int]:
        return [int(ingredient) for ingredient in raw_ingredients]

    @staticmethod
    def _raw_range_to_range(raw_range: str) -> list[int]:
        raw_low, raw_high = raw_range.split('-')
        return [int(raw_low), int(raw_high)]

    @staticmethod
    def _raw_ranges_to_ranges(raw_ranges: list[str]) -> list[list[int]]:
        results = []
        for raw_range in raw_ranges:
            results.append(Day05._raw_range_to_range(raw_range))
        return results

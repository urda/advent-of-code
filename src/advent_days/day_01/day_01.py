"""
Copyright 2022 Peter Urda

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


class Day01(DayMeta):
    """
    Advent of Code 2022, Day 01
    """

    @classmethod
    def _get_data_file_name(cls) -> str:
        return 'day_01.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_01.txt')

        data = cls.parse_data(raw_data)

        return [
            str(cls.compute_part_1(data)),
            str(cls.compute_part_2(data)),
        ]

    @classmethod
    def compute_part_1(cls, parsed_data: List[int]) -> int:
        """
        Get Part 1's Answer

        :param parsed_data: The list of calorie values parsed.
        :returns: The maximum calorie total for the elf with the most.
        """
        return max(parsed_data)

    @classmethod
    def compute_part_2(cls, parsed_data: List[int]) -> int:
        """
        Get Part 2's Answer

        :param parsed_data: The list of calorie values parsed.
        :returns: The sum of the three largest calorie sums.
        """

        results = sorted(parsed_data)
        results = results[-3:]
        return sum(results)

    @classmethod
    def parse_data(cls, raw_data: List[str]) -> List[int]:
        """
        Parse the Day 01 data and convert into an understood format.

        :param raw_data: The raw data from Advent of Code
        :returns: Computed calorie "totals".
        """

        results = []
        running_total = 0
        for data_entry in raw_data:
            if not data_entry:
                results.append(running_total)
                running_total = 0
                continue

            running_total += int(data_entry)

        return results

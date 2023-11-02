"""
Copyright 2023 Peter Urda

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


class Day10(DayMeta):
    """
    Advent of Code 2015, Day 10
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_10.txt')[0]
        data = cls._parse_to_ints(raw_data)

        return [
            str(cls.compute_part_1(data)),
            str(cls.compute_part_2(data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[int]) -> int:
        """
        Parse the data and compute for Day 10.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return len(cls._perform_look_and_say(data, 40))

    @classmethod
    def compute_part_2(cls, data: List[int]) -> int:
        """
        Parse the data and compute for Day 10.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return len(cls._perform_look_and_say(data, 50))

    @classmethod
    def _parse_to_ints(cls, data: str) -> List[int]:
        return [int(x) for x in data]

    @classmethod
    def _perform_look_and_say(cls, data: List[int], rounds: int) -> List[int]:
        for _ in range(rounds):
            data = cls._perform_look_and_say_round(data)
        return data

    @classmethod
    def _perform_look_and_say_round(cls, data: List[int]) -> List[int]:
        results = []
        seen = -1
        tracked = None

        for curr_val in data:
            if not tracked:
                tracked = curr_val
                seen = 1
                continue
            if tracked == curr_val:
                seen += 1
                continue

            # So the values don't match. Report the current 'results'
            # and reset for the next character seen.
            results.extend([seen, tracked])
            tracked = curr_val
            seen = 1

        results.extend([seen, tracked])  # Catch the open counters left over
        return results

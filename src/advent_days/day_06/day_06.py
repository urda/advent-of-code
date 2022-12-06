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


class Day06(DayMeta):
    """
    Advent of Code 2022, Day 06
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_06.txt')[0]

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, elf_datastream: str) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param elf_datastream: The raw data from Advent of Code
        :returns: The result for Part 1
        """
        return cls._search_data(elf_datastream, 4)

    @classmethod
    def compute_part_2(cls, elf_datastream: str) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param elf_datastream: The raw data from Advent of Code
        :returns: The result for Part 2
        """
        return cls._search_data(elf_datastream, 14)

    @classmethod
    def _search_data(cls, elf_datastream, msg_size: int) -> int:
        """
        Given the elf datastream, search the message for the unique sets

        :param elf_datastream: The string of data from the elves to search.
        :param msg_size: The number of unique characters needed to be seen.
        :return: The number of characters seen after finding the marker.
        """

        local_line = []
        result = -1

        for idx, elf_char in enumerate(elf_datastream):
            local_line.append(elf_char)

            if len(local_line) < msg_size:
                continue

            if len(set(local_line)) == msg_size:
                result = idx + 1
                break

            local_line.pop(0)

        return result

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

from collections import defaultdict
from typing import List

from ..day_meta import DayMeta


class Day07(DayMeta):
    """
    Advent of Code 2025, Day 07
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_07.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 07.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        if len(data) <= 0:
            raise ValueError

        init_line = data[0]
        start_pos = init_line.index('S')
        tracking_beams = {start_pos}
        split_count = 0

        for line_data in data[1:]:
            tracking_beam_list = list(tracking_beams)
            for pos in tracking_beam_list:
                if line_data[pos] == '^':
                    tracking_beams.add(pos-1)
                    tracking_beams.add(pos+1)
                    tracking_beams.remove(pos)
                    split_count += 1

        return split_count

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 07.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        if len(data) <= 0:
            raise ValueError

        init_line = data[0]
        start_pos = init_line.index('S')
        tracking_worlds = defaultdict(int)
        tracking_worlds[start_pos] = 1

        for line_data in data[1:]:
            tracking_beam_list = list(tracking_worlds.keys())
            for pos in tracking_beam_list:
                worlds = tracking_worlds[pos]
                if line_data[pos] == '^':
                    tracking_worlds[pos-1] += worlds
                    tracking_worlds[pos+1] += worlds
                    del tracking_worlds[pos]

        worlds = sum(tracking_worlds.values())
        return worlds

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

from math import lcm
from typing import (
    Callable,
    List,
)

from .wasteland_map import WastelandMap
from ..day_meta import DayMeta


class Day08(DayMeta):
    """
    Advent of Code 2023, Day 08
    """

    _START_CHAR = 'A'
    _END_CHAR = 'Z'

    _START_COORD = 'AAA'
    _END_COORD = 'ZZZ'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_08.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 08.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        wasteland = WastelandMap.from_string(data)
        return cls._navigate_map(
            wasteland,
            cls._START_COORD,
            lambda x: x == cls._END_COORD
        )

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 08.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        wasteland = WastelandMap.from_string(data)
        return cls._navigate_map_many(wasteland)

    @classmethod
    def _navigate_map(
            cls,
            data_map: WastelandMap,
            start_coord: str,
            is_terminal_func: Callable,
    ) -> int:
        steps_taken = 0
        found_end = False
        travel_pointer = data_map.nodes[start_coord]

        while not found_end:
            for next_step in data_map.directions:
                match next_step:
                    case 'L':
                        next_node = data_map.nodes[travel_pointer.left]
                    case 'R':
                        next_node = data_map.nodes[travel_pointer.right]
                    case _:
                        raise ValueError(f'Invalid Direction: {next_step}')
                steps_taken += 1
                travel_pointer = next_node

            if is_terminal_func(travel_pointer.location_id):
                found_end = True

        return steps_taken

    @classmethod
    def _navigate_map_many(cls, data_map: WastelandMap) -> int:
        start_keys = []
        for wasteland_keys in data_map.nodes.keys():
            if wasteland_keys.endswith(cls._START_CHAR):
                start_keys.append(wasteland_keys)

        ghosts = []
        for start_key in start_keys:
            ghosts.append(
                cls._navigate_map(
                    data_map,
                    start_key,
                    lambda x: x.endswith(cls._END_CHAR)
                )
            )

        return lcm(*ghosts)

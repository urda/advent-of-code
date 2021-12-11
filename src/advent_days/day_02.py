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

from typing import (
    List,
    Tuple,
)

from .day_meta import DayMeta


class Day02(DayMeta):
    """
    Advent Day 02
    """

    _data_file = 'day_02.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        commands = cls.get_lines_as_list_string(cls._data_file)

        part_1_horizontal_pos, part_1_depth_pos = cls.perform_part_1(commands)
        part_2_horizontal_pos, part_2_depth_pos = cls.perform_part_2(commands)

        return [
            'Part 1:',
            f'Determined Horizontal: {part_1_horizontal_pos}',
            f'Determined Depth: {part_1_depth_pos}',
            f'Determined: {part_1_horizontal_pos * part_1_depth_pos}',
            '---',
            'Part 2',
            f'Determined Horizontal: {part_2_horizontal_pos}',
            f'Determined Depth: {part_2_depth_pos}',
            f'Determined: {part_2_horizontal_pos * part_2_depth_pos}',
        ]

    @classmethod
    def perform_part_1(cls, commands: List[str]) -> Tuple[int, int]:
        """
        Compute the answer to part 1 for Day 02.

        :param commands: The commands to process as a list of strings.
        :return: The result as a tuple: (horizontal position, depth position)
        """

        horizontal_pos = 0
        depth_pos = 0

        for command in commands:
            raw_direction, raw_distance = command.split(' ')
            direction = raw_direction.lower()
            distance = int(raw_distance)

            match direction:
                case 'down':
                    depth_pos += distance
                case 'forward':
                    horizontal_pos += distance
                case 'up':
                    depth_pos -= distance
                case _:
                    raise ValueError(f'Cannot process command "{direction}"')

        return horizontal_pos, depth_pos

    @classmethod
    def perform_part_2(cls, commands: List[str]) -> Tuple[int, int]:
        """
        Compute the answer to part 2 for Day 02.

        :param commands: The commands to process as a list of strings.
        :return: The result as a tuple: (horizontal position, depth position)
        """

        horizontal_pos = 0
        depth_pos = 0
        aim_value = 0

        for command in commands:
            raw_direction, raw_distance = command.split(' ')
            direction = raw_direction.lower()
            distance = int(raw_distance)

            match direction:
                case 'down':
                    aim_value += distance
                case 'forward':
                    horizontal_pos += distance
                    depth_pos += aim_value * distance
                case 'up':
                    aim_value -= distance
                case _:
                    raise ValueError(f'Cannot process command "{direction}"')

        return horizontal_pos, depth_pos

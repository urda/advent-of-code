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

from typing import (
    List,
)

from .xmas_light import XmasLight
from .xmas_light_bright import XmasLightBright
from .xmas_light_instruction import XmasLightInstruction
from .xmas_light_operation import XmasLightOperation
from ..day_meta import DayMeta


class Day06(DayMeta):
    """
    Advent of Code 2015, Day 06
    """

    _grid_limit = 1000
    _split_key_coords = ','
    _split_key_through = ' through '

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_06.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 06.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        grid: list[list[XmasLight]] = cls._build_grid()
        instructions = cls._parse(data)

        for instruction in instructions:
            for pos_x in instruction.range_x:
                for pos_y in instruction.range_y:
                    match instruction.operation:
                        case XmasLightOperation.TOGGLE:
                            grid[pos_x][pos_y].toggle()
                        case XmasLightOperation.TURN_ON:
                            grid[pos_x][pos_y].on = True
                        case XmasLightOperation.TURN_OFF:
                            grid[pos_x][pos_y].on = False

        return cls._count_grid(grid)

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 06.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        grid: list[list[XmasLightBright]] = cls._build_brightness_grid()
        instructions = cls._parse(data)

        for instruction in instructions:
            for pos_x in instruction.range_x:
                for pos_y in instruction.range_y:
                    match instruction.operation:
                        case XmasLightOperation.TOGGLE:
                            grid[pos_x][pos_y].toggle()
                        case XmasLightOperation.TURN_ON:
                            grid[pos_x][pos_y].set_on()
                        case XmasLightOperation.TURN_OFF:
                            grid[pos_x][pos_y].set_off()

        return cls._count_brightness_grid(grid)

    @classmethod
    def _build_brightness_grid(cls) -> List[List[XmasLightBright]]:
        """Init a new Xmas Light (Brightness variant) Grid"""
        results = []
        for pos_x in range(cls._grid_limit):
            curr_row = []
            for pos_y in range(cls._grid_limit):
                curr_row.append(XmasLightBright(pos_x, pos_y))
            results.append(curr_row)
        return results

    @classmethod
    def _build_grid(cls) -> List[List[XmasLight]]:
        """Init a new Xmas Light Grid"""
        results = []
        for pos_x in range(cls._grid_limit):
            curr_row = []
            for pos_y in range(cls._grid_limit):
                curr_row.append(XmasLight(pos_x, pos_y))
            results.append(curr_row)
        return results

    @classmethod
    def _count_brightness_grid(cls, grid: List[List[XmasLightBright]]) -> int:
        """
        Given an Xmas Light (Brightness variant) grid, report the brightness.

        :param grid: The brightness grid to search
        :return: The total brightness of the grid.
        """
        results = 0
        for pos_x in range(cls._grid_limit):
            for pos_y in range(cls._grid_limit):
                results += grid[pos_x][pos_y].brightness
        return results

    @classmethod
    def _count_grid(cls, grid: List[List[XmasLight]]) -> int:
        """
        Given an Xmas Light grid, count the number of ON lights.

        :param grid: The grid to search.
        :return: The number of "on" lights in the grid.
        """
        results = 0
        for pos_x in range(cls._grid_limit):
            for pos_y in range(cls._grid_limit):
                if grid[pos_x][pos_y].on:
                    results += 1
        return results

    @classmethod
    def _parse(cls, data: List[str]) -> List[XmasLightInstruction]:
        """
        Given a group of instructions, parse all into an understood format.

        :param data: The raw list of instructions to parse.
        :return: A parsed XmasLightInstruction list.
        """
        results = []
        for instruction_entry in data:
            results.append(cls._parse_instruction(instruction_entry))
        return results

    @classmethod
    def _parse_instruction(cls, data: str) -> XmasLightInstruction:
        """
        Given a single raw instruction, parse into an understood format.

        :param data: The single instruction to parse.
        :return: A parsed XmasLightInstruction.
        """
        if data[4] == 'l':
            xmas_op = XmasLightOperation.TOGGLE
            slice_mark = 7
        elif data[6] == 'n':
            xmas_op = XmasLightOperation.TURN_ON
            slice_mark = 8
        elif data[6] == 'f':
            xmas_op = XmasLightOperation.TURN_OFF
            slice_mark = 9
        else:
            raise ValueError

        raw_x, raw_y = data[slice_mark::].split(cls._split_key_through)
        x_start, y_start = [int(x) for x in raw_x.split(cls._split_key_coords)]
        x_end, y_end = [int(y) for y in raw_y.split(cls._split_key_coords)]
        x_range = range(x_start, x_end + 1)
        y_range = range(y_start, y_end + 1)

        return XmasLightInstruction(xmas_op, x_range, y_range)

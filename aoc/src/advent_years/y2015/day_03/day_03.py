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

from advent_common.coordinate import Coordinate
from advent_common.pointer import Pointer
from .cardinaldirection import CardinalDirection
from ..day_meta import DayMeta


class Day03(DayMeta):
    """
    Advent of Code 2015, Day 03
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_03.txt')[0]

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: str) -> int:
        """
        Parse the data and convert into an understood format and compute.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        santas_sleigh: Pointer = Pointer(0, 0)
        visited: set[Coordinate] = {santas_sleigh.coordinate}

        for raw_direction in data:
            direction = CardinalDirection.convert_to_direction(raw_direction)
            cls._step_sleigh(santas_sleigh, direction)
            visited.add(santas_sleigh.coordinate)

        return len(visited)

    @classmethod
    def compute_part_2(cls, data: str) -> int:
        """
        Parse the data and convert into an understood format and compute.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        santas_sleigh: Pointer = Pointer(0, 0)
        robo_sleigh: Pointer = Pointer(0, 0)
        visited: set[Coordinate] = {
            santas_sleigh.coordinate,
            robo_sleigh.coordinate,
        }

        santas_turn = True
        for raw_direction in data:
            direction = CardinalDirection.convert_to_direction(raw_direction)

            if santas_turn:
                cls._step_sleigh(santas_sleigh, direction)
                new_coord = santas_sleigh.coordinate
            else:
                cls._step_sleigh(robo_sleigh, direction)
                new_coord = robo_sleigh.coordinate
            santas_turn = not santas_turn

            visited.add(new_coord)

        return len(visited)

    @classmethod
    def _step_sleigh(cls, sleigh_ptr: Pointer, direction: CardinalDirection):
        match direction:
            case CardinalDirection.NORTH:
                sleigh_ptr.y += 1
            case CardinalDirection.SOUTH:
                sleigh_ptr.y -= 1
            case CardinalDirection.EAST:
                sleigh_ptr.x += 1
            case CardinalDirection.WEST:
                sleigh_ptr.x -= 1

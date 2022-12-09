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
    Set,
)

from .coordinate import Coordinate
from .direction import Direction
from .linked_pointer import LinkedPointer
from .movement import Movement
from .pointer import Pointer
from ..day_meta import DayMeta


class Day09(DayMeta):
    """
    Advent of Code 2022, Day 09
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_09.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        movements = cls._parse(data)
        h_pointer = Pointer(0, 0)
        t_pointer = Pointer(0, 0)

        tail_touched = set()
        for instruction in movements:
            tail_touched.update(
                cls._pull_rope(h_pointer, t_pointer, instruction)
            )

        return len(tail_touched)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        movements = cls._parse(data)
        h_pointer = LinkedPointer(0, 0, None)
        t_pointer = LinkedPointer(0, 0, None)

        curr_pointer = h_pointer
        for _ in range(8):
            new_segment = LinkedPointer(0, 0, None)
            curr_pointer.next = new_segment
            curr_pointer = new_segment
        curr_pointer.next = t_pointer

        tail_touched = set()
        for instruction in movements:
            tail_touched.update(
                cls._pull_rope(h_pointer, t_pointer, instruction)
            )

        return len(tail_touched)

    @classmethod
    def _parse(cls, raw_data: List[str]) -> List[Movement]:
        results = []
        for raw_data_line in raw_data:
            results.append(Movement(raw_data_line))
        return results

    @classmethod
    def _pull_rope(
            cls,
            head_pointer: Pointer,
            tail_pointer: Pointer,
            movement: Movement,
    ) -> Set[Coordinate]:
        direction: Direction = movement.direction
        steps: int = movement.steps

        single_step: int = 1
        results: Set[Coordinate] = set()

        for _ in range(steps):
            match direction:
                case Direction.UP:
                    head_pointer.y += single_step
                case Direction.RIGHT:
                    head_pointer.x += single_step
                case Direction.DOWN:
                    head_pointer.y -= single_step
                case Direction.LEFT:
                    head_pointer.x -= single_step
                case _:
                    raise ValueError

            if isinstance(head_pointer, LinkedPointer):
                curr_node = head_pointer
                next_node = curr_node.next

                while next_node:
                    cls._update_tail(curr_node, next_node)
                    curr_node = next_node
                    next_node = curr_node.next
            else:
                cls._update_tail(head_pointer, tail_pointer)

            results.add(tail_pointer.coordinate)

        return results

    @classmethod
    def _update_tail(
            cls,
            h_pointer: Pointer,
            t_pointer: Pointer,
    ):
        diff_x = h_pointer.x - t_pointer.x
        diff_y = h_pointer.y - t_pointer.y

        # Neighbors do nothing
        if abs(diff_x) <= 1 and abs(diff_y) <= 1:
            return

        # Horizontal lock
        if diff_x == 0:
            t_pointer.y += diff_y // abs(diff_y)

        # Vertical lock
        elif diff_y == 0:
            t_pointer.x += diff_x // abs(diff_x)

        # Angled movement
        else:
            t_pointer.x += diff_x // abs(diff_x)
            t_pointer.y += diff_y // abs(diff_y)

        return

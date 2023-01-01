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

from .node import Node
from ..day_meta import DayMeta


class Day20(DayMeta):
    """
    Advent of Code 2022, Day 20
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_int('day_20.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[int]) -> int:
        """
        Parse the data and compute for Day 20.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        values = cls._parse(data)
        return cls._mix(values)

    @classmethod
    def compute_part_2(cls, data: List[int]) -> int:
        """
        Parse the data and compute for Day 20.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        values = cls._parse(data)
        for num in values:
            num.value *= 811589153
        return cls._mix(values, 10)

    @classmethod
    def _mix(cls, message: List[Node], times: int = 1):
        numbers, message_size = list(message), len(message)

        for _ in range(times):
            for node in message:
                i = numbers.index(node)
                numbers.pop(i)
                numbers.insert((i + node.value) % (message_size - 1), node)

        idx_zero = None
        for idx_zero, node in enumerate(numbers):
            if node.value == 0:
                break

        return sum(
            numbers[(idx_zero + delta) % message_size].value
            for delta in (1000, 2000, 3000)
        )

    @classmethod
    def _parse(cls, raw_data: List[int]) -> List[Node]:
        return [Node(x) for x in raw_data]

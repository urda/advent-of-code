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

import sys
from heapq import (
    heappop,
    heappush,
)
from typing import (
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day17(DayMeta):
    """
    Advent of Code 2023, Day 17
    """

    _DIRECTIONS = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_of_integer_lists('day_17.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[List[int]]) -> int:
        """
        Parse the data and compute for Day 17.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._walk_crucible(data, 1, 3)

    @classmethod
    def compute_part_2(cls, data: List[List[int]]) -> int:
        """
        Parse the data and compute for Day 17.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._walk_crucible(data, 4, 10)

    @classmethod
    def _is_in_range(cls, pos: Tuple[int, int], data: List[List[int]]) -> bool:
        return pos[0] in range(len(data)) and pos[1] in range(len(data[0]))

    # pylint: disable=too-many-locals
    @classmethod
    def _walk_crucible(
            cls,
            data: List[List[int]],
            min_steps: int,
            max_steps: int
    ) -> int:
        costs = {}
        seen = set()
        queue = [(0, 0, 0, -1)]
        while queue:
            cost, x, y, disallowed_dir = heappop(queue)

            if x == len(data) - 1 and y == len(data[0]) - 1:
                return cost

            if (x, y, disallowed_dir) in seen:
                continue
            seen.add((x, y, disallowed_dir))

            for direction, _ in enumerate(cls._DIRECTIONS):
                cost_increase = 0

                if disallowed_dir in (direction, (direction + 2) % 4):
                    continue

                for distance in range(1, max_steps + 1):
                    next_x = x + cls._DIRECTIONS[direction][0] * distance
                    next_y = y + cls._DIRECTIONS[direction][1] * distance

                    if cls._is_in_range((next_x, next_y), data):
                        cost_increase += data[next_x][next_y]
                        if distance < min_steps:
                            continue

                        new_cost = cost + cost_increase
                        cost_comp = costs.get(
                            (next_x, next_y, direction), sys.maxsize
                        )
                        if cost_comp <= new_cost:
                            continue

                        costs[(next_x, next_y, direction)] = new_cost
                        heappush(queue, (new_cost, next_x, next_y, direction))
        return 0

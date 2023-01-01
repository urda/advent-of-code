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
from collections import defaultdict
from typing import List

from ..day_meta import DayMeta


class Day24(DayMeta):
    """
    Advent of Code 2022, Day 24
    """

    _directions = {
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0),
        '^': (-1, 0),
    }

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_24.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data):
        """
        Parse the data and compute for Day 24.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        blizzard = cls._parse(data)
        time_to_goal, _ = cls._travel_to_goal(blizzard, data)
        return time_to_goal

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 24.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        height, width = len(data) - 2, len(data[0]) - 2
        src, dst = (-1, 0), (height, width - 1)

        blizzard = cls._parse(data)
        time_to_goal, blizzard = cls._travel_to_goal(blizzard, data)
        time_to_start, blizzard = cls._bfs(blizzard, dst, src, height, width)
        time_back_goal, blizzard = cls._travel_to_goal(blizzard, data)
        return time_to_goal + time_to_start + time_back_goal

    @classmethod
    def _advance(cls, bliz, positions, height, width):
        for pos in positions:
            yield from cls._neighbors(bliz, *pos, height, width)

    @classmethod
    def _bfs(cls, bliz, src, dst, height, width):
        # pylint: disable=too-many-arguments

        positions = {src}
        time = 0

        while dst not in positions:
            time += 1
            bliz = cls._evolve_blizzard(bliz, width, height)
            positions = set(cls._advance(bliz, positions, height, width))

        return time, bliz

    @classmethod
    def _evolve_blizzard(cls, bliz, width, height):
        # pylint: disable=invalid-name

        new = defaultdict(list)

        for (r, c), dirs in bliz.items():
            for dr, dc in dirs:
                new[(r + dr) % height, (c + dc) % width].append((dr, dc))

        return new

    @classmethod
    def _neighbors(cls, bliz, r, c, height, width):
        # pylint: disable=invalid-name
        # pylint: disable=too-many-arguments

        if r == 0 and c == 0:
            yield -1, 0
        elif r == height - 1 and c == width - 1:
            yield height, c

        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < height and 0 <= cc < width and (rr, cc) not in bliz:
                yield rr, cc

        if (r, c) not in bliz:
            yield r, c

    @classmethod
    def _parse(cls, data):
        # pylint: disable=invalid-name

        results = defaultdict(list)
        for r, row in enumerate(data[1:-1]):
            for c, cell in enumerate(row[1:-1]):
                if cell in cls._directions:
                    results[r, c].append(cls._directions[cell])
        return results

    @classmethod
    def _travel_to_goal(cls, blizzard, blizzard_data):
        height, width = len(blizzard_data) - 2, len(blizzard_data[0]) - 2
        src, dst = (-1, 0), (height, width - 1)

        time, blizzard = cls._bfs(blizzard, src, dst, height, width)
        return time, blizzard

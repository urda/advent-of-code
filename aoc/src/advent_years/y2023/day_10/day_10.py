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

from typing import (
    Dict,
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day10(DayMeta):
    """
    Advent of Code 2023, Day 10
    """

    _START_CHAR = 'S'

    _PIPE_DIRS = {
        "|": [1, -1],
        "-": [1j, -1j],
        "J": [-1, -1j],
        "F": [1, 1j],
        "7": [1, -1j],
        "L": [-1, 1j],
        _START_CHAR: [1, 1j],
    }

    _DIRECTIONS = (0, -1), (0, 1), (-1, 0), (1, 0)
    _UP, _DOWN, _LEFT, _RIGHT = _DIRECTIONS
    _CONNECTIONS = {
        '|': (_UP, _DOWN),
        '-': (_LEFT, _RIGHT),
        '7': (_LEFT, _DOWN),
        'J': (_LEFT, _UP),
        'L': (_UP, _RIGHT),
        'F': (_RIGHT, _DOWN),
    }

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_10.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 10.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return len(cls._loop_path(*cls._parse(data))) // 2

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 10.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._area_inner(cls._loop_path(*cls._parse(data)))

    @classmethod
    def _area_inner(cls, border: List[Tuple[int, int]]):
        """
        Given the border, use Shoelace and Pick's to find the answer.
        """
        border_length = len(border)
        x, y = zip(*border)

        # Shoelace formula
        # https://en.wikipedia.org/wiki/Shoelace_formula
        area = abs(sum(
            x[i] * y[(i + 1) % border_length]
            - y[i] * x[(i + 1) % border_length]
            for i in range(border_length)
        )) // 2

        # Pick's theorem
        # https://en.wikipedia.org/wiki/Pick%27s_theorem
        return area - border_length // 2 + 1

    @classmethod
    def _loop_path(
            cls,
            graph: Dict[Tuple[int, int], List[Tuple[int, int]]],
            start: Tuple[int, int],
    ):
        """
        Travel the path until empty.
        """
        path = [start]
        next_val = graph[start][0]
        while next_val != start:
            path.append(next_val)
            next_val = next(
                next_jump for next_jump in graph[next_val]
                if next_jump != path[-2]
            )
        return path

    @classmethod
    def _parse(cls, data: List[str]):
        """
        Parse the map, and connect valid cells.
        """
        graph = {}
        start = start_x = start_y = None
        for y_idx, data_line in enumerate(data):
            for x_idx, data_value in enumerate(data_line):
                if data_value == cls._START_CHAR:
                    start = start_x, start_y = x_idx, y_idx

                # Record the connection if it's present, empty otherwise
                graph[(x_idx, y_idx)] = [
                    (x_idx + dx, y_idx + dy)
                    for dx, dy in cls._CONNECTIONS.get(data_value, ())
                ]

        graph[start] = [
            (start_x + dx, start_y + dy) for dx, dy in cls._DIRECTIONS
            if start in graph.get((start_x + dx, start_y + dy), [])
        ]

        return graph, start

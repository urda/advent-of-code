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

from itertools import pairwise
from typing import (
    List,
    Tuple,
)

from .dig_plan_step import DigPlanStep
from ..day_meta import DayMeta


class Day18(DayMeta):
    """
    Advent of Code 2023, Day 18
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_18.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 18.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._dig_area(data, False)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 18.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._dig_area(data, True)

    @classmethod
    def _compute_points_inside_polygon(
            cls,
            area: int,
            number_of_edges: int
    ) -> int:
        """
        Pick's Theorem expresses the area of a polygon, all of whose
        vertices are lattice points in a coordinate plane, in terms of
        the number of lattice points inside the polygon and the number
        of lattice points on the sides of the polygon.

        Source: https://en.wikipedia.org/wiki/Pick%27s_theorem
        """

        return int(area - number_of_edges // 2 + 1)

    @classmethod
    def _compute_polygon_area(cls, vertices: List[Tuple[int, int]]) -> int:
        """
        Use the "Triangle Formula" to compute the area of the polygon.

        Source:
        https://en.m.wikipedia.org/wiki/Shoelace_formula#Triangle_formula
        """
        area = 0

        for (x1, y1), (x2, y2) in pairwise(vertices + [vertices[0]]):
            area += x1 * y2 - x2 * y1

        return int(area // 2)

    @classmethod
    def _compute_polygon_area_positive(
            cls,
            vertices: List[Tuple[int, int]]
    ) -> int:
        """
        If the vertices are not counter-clockwise, it's negative.
        Reverse and run again if required.
        """
        if (area := cls._compute_polygon_area(vertices)) >= 0:
            return area

        return cls._compute_polygon_area(vertices[::-1])

    @classmethod
    def _dig_area(cls, raw_dig_plan: List[str], decode_hex: bool = False):
        dig_plan = []
        for data_line in raw_dig_plan:
            dig_plan.append(DigPlanStep(data_line, decode_hex))

        vertices, length = cls._trench_vertices(dig_plan)
        built_vertices = [(int(z.real), int(z.imag)) for z in vertices]
        area = cls._compute_polygon_area_positive(built_vertices)
        points = cls._compute_points_inside_polygon(area, length)

        # Add the border, and points inside the area.
        return points + length

    @classmethod
    def _trench_vertices(
            cls,
            dig_plan: List[DigPlanStep]
    ) -> Tuple[List[int], int]:
        """
        Given all the dig plan steps,
        compute the vertices and length travelled.
        """
        vertexes, length = [0], 0

        for dig_step in dig_plan:
            steps = dig_step.steps
            length += dig_step.steps
            match dig_step.direction:
                case 'R':
                    vertexes.append(vertexes[-1] - steps)
                case 'L':
                    vertexes.append(vertexes[-1] + steps)
                case 'U':
                    vertexes.append(vertexes[-1] - steps * 1j)
                case 'D':
                    vertexes.append(vertexes[-1] + steps * 1j)

        return vertexes, length

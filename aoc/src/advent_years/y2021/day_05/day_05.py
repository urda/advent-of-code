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

from .vent_line import VentLine
from .vent_point import VentPoint
from ..day_meta import DayMeta


class Day05(DayMeta):
    """
    Advent Day 05
    """

    _data_file = 'day_05.txt'

    _delimiter = '->'
    _point_delimiter = ','

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_sum = cls.perform_work(
            cls.get_lines_as_list_string(cls._data_file),
            False,
        )

        part_2_sum = cls.perform_work(
            cls.get_lines_as_list_string(cls._data_file),
            True,
        )

        return [
            'Part 1:',
            f'Determined: {part_1_sum}',
            '---',
            'Part 2:',
            f'Determined: {part_2_sum}',
        ]

    @classmethod
    def perform_work(
            cls,
            vent_data: List[str],
            include_diagonals: bool
    ) -> int:
        """
        Perform work for this Day 05. Works for both portions.

        :param vent_data: The vent data as a list of strings.
        :param include_diagonals: Set to 'True' if diagonals should be
                                  considered.
        :return: The number of multiple line overlap points.
        """

        vent_lines, vent_dimensions = cls._build_vent_data(vent_data)
        vent_map = [
            [0 for _0 in range(vent_dimensions[0])]
            for _1 in range(vent_dimensions[1])
        ]
        return cls._process_vent_lines(vent_lines, vent_map, include_diagonals)

    @classmethod
    def _build_line(cls, raw_data: str) -> VentLine:
        point_a, point_b = cls._build_points(raw_data)
        return VentLine(point_a, point_b)

    @classmethod
    def _build_points(cls, raw_data: str) -> Tuple[VentPoint, VentPoint]:
        line_entry_no_newline = raw_data.strip()
        point_a, point_b = line_entry_no_newline.split(cls._delimiter)

        point_a_x_raw, point_a_y_raw = point_a.split(cls._point_delimiter)
        point_b_x_raw, point_b_y_raw = point_b.split(cls._point_delimiter)

        point_a_x, point_a_y = int(point_a_x_raw), int(point_a_y_raw)
        point_b_x, point_b_y = int(point_b_x_raw), int(point_b_y_raw)

        return VentPoint(point_a_x, point_a_y), VentPoint(point_b_x, point_b_y)

    @classmethod
    def _build_vent_data(
            cls,
            raw_data: List[str]
    ) -> Tuple[List[VentLine], Tuple[int, int]]:
        results = []
        largest_x = -1
        largest_y = -1

        for line_entry_raw in raw_data:
            vent_line = cls._build_line(line_entry_raw)
            point_a_x, point_a_y = vent_line.point_a.x, vent_line.point_a.y
            point_b_x, point_b_y = vent_line.point_b.x, vent_line.point_b.y
            results.append(vent_line)

            # Update our map details
            if point_a_x > largest_x or point_b_x > largest_x:
                largest_x = point_a_x \
                    if point_a_x > largest_x else \
                    point_b_x
            if point_a_y > largest_y or point_b_y > largest_y:
                largest_y = point_a_y \
                    if point_a_y > largest_y else \
                    point_b_y

        return results, (largest_x + 1, largest_y + 1)

    # pylint: disable=invalid-name
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-locals
    @classmethod
    def _process_vent_lines(
            cls,
            vent_lines: List[VentLine],
            vent_map: List[List[int]],
            include_diagonals: bool = False
    ) -> int:
        for vent_line in vent_lines:
            point_a = vent_line.point_a
            point_b = vent_line.point_b

            if point_a.x == point_b.x:
                locked_x = point_a.x
                low_y, high_y = sorted([point_a.y, point_b.y])

                for y in range(low_y, high_y + 1):
                    vent_map[locked_x][y] += 1
            elif point_a.y == point_b.y:
                low_x, high_x = sorted([point_a.x, point_b.x])
                locked_y = point_a.y

                for x in range(low_x, high_x + 1):
                    vent_map[x][locked_y] += 1
            elif include_diagonals:
                if point_a.x <= point_b.x:
                    start_point, end_point = point_a, point_b
                else:
                    start_point, end_point = point_b, point_a

                y = start_point.y
                for x in range(start_point.x, end_point.x + 1):
                    vent_map[x][y] += 1

                    if end_point.y >= start_point.y:
                        y += 1
                    else:
                        y -= 1

        multipoints_seen = 0
        for row in vent_map:
            for cell in row:
                if cell > 1:
                    multipoints_seen += 1

        return multipoints_seen

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


class Day09(DayMeta):
    """
    Advent Day 09
    """

    _data_file = 'day_09.txt'

    @classmethod
    def get_lava_map_dimensions(
            cls,
            lava_map: List[List[int]]
    ) -> Tuple[int, int]:
        """
        Determine the width and height of the lava tube map.

        :param lava_map: The lava tube map being processed.
        :return: The dimensions of the map as a tuple (height, width).
        """

        widths = set(map(len, lava_map))
        if len(widths) != 1:
            raise ValueError('Lava tubes map is malformed.')
        height = len(lava_map)
        width = widths.pop()

        return height, width

    @classmethod
    def is_laval_cell_lower(
            cls,
            lava_map: List[List[int]],
            column_pos: int,
            row_pos: int
    ) -> bool:
        """
        Given a lava map and desired point, determine if this point is lower
        than their neighbors

        :param lava_map: The lava tube map being processed.
        :param column_pos: The column position being looked at.
        :param row_pos: The row position being looked at.
        :return: 'True if it is lower than all their neighbors,
                 'False' otherwise.
        """

        lava_map_height, lava_map_width = cls.get_lava_map_dimensions(lava_map)
        current_value = lava_map[row_pos][column_pos]

        neighbors = []
        # North
        if row_pos - 1 >= 0:
            neighbors.append(lava_map[row_pos - 1][column_pos])
        # South
        if row_pos + 1 < lava_map_height:
            neighbors.append(lava_map[row_pos + 1][column_pos])
        # East
        if column_pos + 1 < lava_map_width:
            neighbors.append(lava_map[row_pos][column_pos + 1])
        # West
        if column_pos - 1 >= 0:
            neighbors.append(lava_map[row_pos][column_pos - 1])

        is_a_low_point = all(current_value < x for x in neighbors)
        return is_a_low_point

    @classmethod
    def process_lava_tube_map(cls, lava_map: List[List[int]]) -> int:
        """
        Given a lava tube map, process and determine the low point sum.

        :param lava_map: The lava map to process.
        :return: The sum of the risk levels of all low points on map.
        """
        lava_map_height, lava_map_width = cls.get_lava_map_dimensions(lava_map)

        result = 0

        for row_pos in range(lava_map_height):
            for column_pos in range(lava_map_width):
                if cls.is_laval_cell_lower(lava_map, column_pos, row_pos):
                    result += 1 + lava_map[row_pos][column_pos]

        return result

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_of_integer_lists(cls._data_file)
        part_1_result = cls.process_lava_tube_map(raw_data)

        return [
            'Part 1:',
            f'Determined: {part_1_result}',
        ]

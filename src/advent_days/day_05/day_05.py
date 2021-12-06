from typing import (
    List,
    Tuple,
)

from .vent_line import VentLine
from .vent_point import VentPoint
from ..day_meta import DayMeta


class Day05(DayMeta):
    _data_file = 'day_05.txt'

    _delimiter = '->'
    _point_delimiter = ','

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_sum = cls._perform_part_1()

        return [
            'Part 1:',
            f'Determined: {part_1_sum}',
        ]

    @classmethod
    def _get_lines(cls) -> List[str]:
        lines = []
        with open(cls.build_data_file_path(cls._data_file), 'r') as data_file:
            for line in data_file:
                lines.append(line)
        return lines

    @classmethod
    def _perform_part_1(cls) -> int:
        vent_lines, map_dimensions = cls._filter_part_1(cls._get_lines())
        vent_map = [
            [0 for x in range(map_dimensions[0])]
            for _ in range(map_dimensions[1])
        ]

        multipoints_seen = 0

        for vent_line in vent_lines:
            point_a = vent_line.point_a
            point_b = vent_line.point_b

            if point_a.x == point_b.x:
                locked_x = point_a.x
                low_y, high_y = sorted([point_a.y, point_b.y])

                for y in range(low_y, high_y + 1):
                    vent_map[locked_x][y] += 1
                    if vent_map[locked_x][y] == 2:
                        multipoints_seen += 1

            elif point_a.y == point_b.y:
                low_x, high_x = sorted([point_a.x, point_b.x])
                locked_y = point_a.y

                for x in range(low_x, high_x + 1):
                    vent_map[x][locked_y] += 1
                    if vent_map[x][locked_y] == 2:
                        multipoints_seen += 1

        return multipoints_seen

    @classmethod
    def _filter_part_1(
            cls,
            raw_data: List[str]
    ) -> Tuple[List[VentLine], Tuple[int, int]]:
        results = []
        largest_x = -1
        largest_y = -1

        for line_entry_raw in raw_data:
            line_entry_no_newline = line_entry_raw.strip()
            point_a, point_b = line_entry_no_newline.split(cls._delimiter)

            point_a_x_raw, point_a_y_raw = point_a.split(cls._point_delimiter)
            point_b_x_raw, point_b_y_raw = point_b.split(cls._point_delimiter)

            point_a_x, point_a_y = int(point_a_x_raw), int(point_a_y_raw)
            point_b_x, point_b_y = int(point_b_x_raw), int(point_b_y_raw)

            if (point_a_x == point_b_x) or (point_a_y == point_b_y):
                # Record the points and line
                line_point_a = VentPoint(point_a_x, point_a_y)
                line_point_b = VentPoint(point_b_x, point_b_y)
                vent_line = VentLine(line_point_a, line_point_b)
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

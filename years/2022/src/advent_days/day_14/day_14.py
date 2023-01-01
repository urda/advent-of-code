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
from copy import deepcopy
from typing import (
    List,
    Set,
    Tuple,
)

from ..day_meta import DayMeta


class Day14(DayMeta):
    """
    Advent of Code 2022, Day 14
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_14.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]):
        """
        Parse the data and compute for Day 14.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        area_map = cls._parse_coord_lines(data)
        known_coords = cls._build_sand_lut(area_map)
        return cls._sim_sand(known_coords)

    @classmethod
    def compute_part_2(cls, data: List[str]):
        """
        Parse the data and compute for Day 14.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        area_map = cls._parse_coord_lines(data)
        known_coords = cls._build_sand_lut(area_map)
        return cls._sim_sand(known_coords, parse_mode=2)

    @classmethod
    def _build_sand_lut(
            cls,
            parsed_coords: List[List[Tuple[int, int]]],
    ) -> Set[Tuple[int, int]]:
        seen_coords = set()

        for coord_line_entry in parsed_coords:
            line_entry_count = len(coord_line_entry)
            start_ptr = 0
            end_ptr = 1

            while end_ptr < line_entry_count:
                start_coord = coord_line_entry[start_ptr]
                end_coord = coord_line_entry[end_ptr]
                line_coords = cls._build_line_coords(start_coord, end_coord)

                for line_coord in line_coords:
                    seen_coords.add(line_coord)

                start_ptr += 1
                end_ptr += 1

        return seen_coords

    @classmethod
    def _build_line_coords(
            cls,
            start_coord: Tuple[int, int],
            end_coord: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        results = []
        diff_x = abs(start_coord[0] - end_coord[0])
        diff_y = abs(start_coord[1] - end_coord[1])

        if diff_x != 0 and diff_y != 0:
            raise ValueError('Improper Line')

        if diff_x == 0:
            # X coords locked
            points = [start_coord[1], end_coord[1]]
            locked_view = start_coord[0]
            range_y = range(min(points), max(points) + 1)

            for y_coord in range_y:
                results.append((locked_view, y_coord))
        else:
            # Y coords locked
            points = [start_coord[0], end_coord[0]]
            locked_view = start_coord[1]
            range_x = range(min(points), max(points) + 1)

            for x_coord in range_x:
                results.append((x_coord, locked_view))

        return results

    @classmethod
    def _parse_coord_lines(
            cls,
            data: List[str]
    ) -> List[List[Tuple[int, int]]]:
        results = []
        for data_entry in data:
            parsed_line = []
            coords = data_entry.split(' -> ')

            for coord_pair in coords:
                raw_x, raw_y = coord_pair.split(',')
                x_pos, y_pos = (int(raw_x), int(raw_y))
                new_coord = (x_pos, y_pos)
                parsed_line.append(new_coord)

            results.append(parsed_line)

        return results

    @classmethod
    def _sim_sand(
            cls,
            area_coords: Set[Tuple[int, int]],
            parse_mode: int = 1,
    ) -> int:
        known_coords = deepcopy(area_coords)
        area_bounds = max(known_coords, key=lambda x: x[1])[1]
        parse_as_part_2 = False

        if parse_mode == 2:
            parse_as_part_2 = True
            area_bounds += 2

        simulating = True
        sand_stops = 0
        while simulating:
            sand_pos_x, sand_pos_y = 500, 0
            sand_falling = True

            while sand_falling:
                if parse_as_part_2 and sand_pos_y + 1 == area_bounds:
                    known_coords.add((sand_pos_x, sand_pos_y))
                    sand_stops += 1
                    sand_falling = False
                elif (sand_pos_x, sand_pos_y) in known_coords \
                        or sand_pos_y > area_bounds:
                    sand_falling = False
                    simulating = False
                elif not (sand_pos_x, sand_pos_y + 1) in known_coords:
                    sand_pos_y = sand_pos_y + 1
                elif not (sand_pos_x - 1, sand_pos_y + 1) in known_coords:
                    sand_pos_x, sand_pos_y = sand_pos_x - 1, sand_pos_y + 1
                elif not (sand_pos_x + 1, sand_pos_y + 1) in known_coords:
                    sand_pos_x, sand_pos_y = sand_pos_x + 1, sand_pos_y + 1
                else:
                    known_coords.add((sand_pos_x, sand_pos_y))
                    sand_stops += 1
                    sand_falling = False

        return sand_stops

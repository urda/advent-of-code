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
    Tuple,
)

from .lava_droplet import LavaDroplet
from ..day_meta import DayMeta


class Day18(DayMeta):
    """
    Advent of Code 2022, Day 18
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
        droplets = cls._parse(data)
        grid = {droplet.coordinates for droplet in droplets}
        return cls._solve_area(grid)

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 18.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        droplets = cls._parse(data)
        grid = {droplet.coordinates for droplet in droplets}
        return cls.surface_scan(grid)

    @classmethod
    def surface_scan(cls, lava_droplets):
        """Perform a surface-level scan to get surface area values."""
        # pylint: disable=too-many-locals

        droplets = frozenset(lava_droplets)
        min_x, min_y, min_z, max_x, max_y, max_z = 0, 0, 0, 0, 0, 0
        for x_pos, y_pos, z_pos in droplets:
            min_x = min(min_x, x_pos)
            max_x = max(max_x, x_pos)
            min_y = min(min_y, y_pos)
            max_y = max(max_y, y_pos)
            min_z = min(min_z, z_pos)
            max_z = max(max_z, z_pos)
        min_x -= 1
        min_y -= 1
        min_z -= 1
        max_x += 1
        max_y += 1
        max_z += 1

        # where can we reach from origin?
        water_points = set()
        search_space = [(min_x, min_y, min_z)]
        while search_space:
            x_pos, y_pos, z_pos = search_space.pop()

            if (x_pos, y_pos, z_pos) in water_points:
                continue
            water_points.add((x_pos, y_pos, z_pos))

            neighbours = LavaDroplet.build_neighborhood(*(x_pos, y_pos, z_pos))
            for neighbor_x, neighbor_y, neighbor_z in neighbours:
                condition_check = (
                        min_x <= neighbor_x <= max_x
                        and min_y <= neighbor_y <= max_y
                        and min_z <= neighbor_z <= max_z
                ) and (
                        (neighbor_x, neighbor_y, neighbor_z) not in droplets
                )
                if condition_check:
                    search_space.append((neighbor_x, neighbor_y, neighbor_z))

        # For any point we can't reach from the start, they have to be inside
        lava_points = set()
        for x_pos in range(min_x, max_x + 1):
            for y_pos in range(min_y, max_y + 1):
                for z_pos in range(min_z, max_z + 1):
                    if (x_pos, y_pos, z_pos) not in water_points:
                        lava_points.add((x_pos, y_pos, z_pos))

        return cls._solve_area(lava_points)

    @classmethod
    def _parse(cls, data: List[str]) -> List[LavaDroplet]:
        results = []
        for data_entry in data:
            raw_x, raw_y, raw_z = data_entry.split(',')
            results.append(LavaDroplet(int(raw_x), int(raw_y), int(raw_z)))
        return results

    @classmethod
    def _solve_area(cls, droplet_coords: Set[Tuple[int, int, int]]):
        droplets = frozenset(droplet_coords)
        result = 0
        for droplet in droplets:
            neighbors = LavaDroplet.build_neighborhood(*droplet)
            for neighbor in neighbors:
                if neighbor not in droplet_coords:
                    result += 1
        return result

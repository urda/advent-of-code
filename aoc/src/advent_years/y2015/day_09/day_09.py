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

import itertools
from collections import defaultdict
from typing import (
    Dict,
    Iterable,
    List,
    Set,
)

from .route_entry import RouteEntry
from ..day_meta import DayMeta


class Day09(DayMeta):
    """
    Advent of Code 2015, Day 09
    """

    # pylint: disable=duplicate-code
    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_09.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 09.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._process_iterations(data, report_mode=0)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 09.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._process_iterations(data, report_mode=1)

    @classmethod
    def _build_distance_lut(
            cls,
            data: Iterable[RouteEntry]
    ) -> Dict[str, Dict[str, int]]:
        results = defaultdict(dict)

        for entry in data:
            results[entry.start][entry.end] = entry.distance
            results[entry.end][entry.start] = entry.distance

        return results

    @classmethod
    def _parse(cls, data: List[str]) -> List[RouteEntry]:
        return [RouteEntry.build_entry(entry) for entry in data]

    @classmethod
    def _parse_unique_cities(cls, data: Iterable[RouteEntry]) -> Set[str]:
        seen = set()
        for entry in data:
            seen.add(entry.start)
            seen.add(entry.end)
        return seen

    @classmethod
    def _process_iterations(
            cls,
            data: List[str],
            report_mode: int = 0
    ) -> int:
        entries = cls._parse(data)
        cities = cls._parse_unique_cities(entries)
        distance_lut = cls._build_distance_lut(entries)

        match report_mode:
            case 0:
                best_value = int(1e20)
            case 1:
                best_value = -1
            case _:
                raise ValueError('Unsupported parse mode!')

        for route_permutation in itertools.permutations(cities):
            total_distance = 0

            for start_idx in range(len(cities) - 1):
                start_city = route_permutation[start_idx]
                end_city = route_permutation[start_idx + 1]
                total_distance += distance_lut[start_city][end_city]

            match report_mode:
                case 0:
                    if total_distance < best_value:
                        best_value = total_distance
                case 1:
                    if total_distance > best_value:
                        best_value = total_distance
                case _:
                    raise ValueError('Unsupported parse mode!')

        return best_value

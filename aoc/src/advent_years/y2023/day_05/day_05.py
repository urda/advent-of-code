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
from typing import (
    Dict,
    List,
    Tuple,
)

from .almanac_map import AlmanacMap
from ..day_meta import DayMeta


class Day05(DayMeta):
    """
    Advent of Code 2023, Day 05
    """

    _start_header = 'seed-to-soil map:'

    _jump_table = {
        'seed-to-soil map:': 'soil-to-fertilizer map:',
        'soil-to-fertilizer map:': 'fertilizer-to-water map:',
        'fertilizer-to-water map:': 'water-to-light map:',
        'water-to-light map:': 'light-to-temperature map:',
        'light-to-temperature map:': 'temperature-to-humidity map:',
        'temperature-to-humidity map:': 'humidity-to-location map:',
        'humidity-to-location map:': None,
    }

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_05.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 05.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        almanac = cls._parse_data(data, False)
        results = {}

        seed: int
        for seed in almanac.seeds:
            results[seed] = cls._seek(almanac, seed)

        return min(results.values())

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 05.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        almanac = cls._parse_data(data, True)
        lowest_loc = sys.maxsize

        seed: Tuple[int, int]
        for seed in almanac.seeds:
            range_start = seed[0]
            range_end = range_start + seed[1]
            for seed_val in range(range_start, range_end):
                new_val = cls._seek(almanac, seed_val)
                if new_val < lowest_loc:
                    lowest_loc = new_val
        return lowest_loc

    @classmethod
    def _seek(cls, book: AlmanacMap, start_val: int) -> int:
        curr_header = cls._start_header
        curr_val = start_val
        while curr_header:
            curr_val = cls._lookup(book, curr_header, curr_val)
            curr_header = cls._jump_table[curr_header]
        return curr_val

    @classmethod
    def _lookup(cls, book: AlmanacMap, curr_header: str, curr_val: int) -> int:
        lut = book.maps[curr_header]

        for lut_range, lut_data in lut.items():
            if curr_val in lut_range:
                # It's there
                offset = curr_val - lut_range.start
                return lut_data[0] + offset

        return curr_val

    @classmethod
    def _parse_data(cls, data: List[str], build_pairs: bool) -> AlmanacMap:
        if build_pairs:
            seeds = cls._parse_seed_pairs(data)
        else:
            seeds = cls._parse_seeds(data)

        return AlmanacMap(
            seeds,
            cls._parse_maps(data),
        )

    @classmethod
    def _parse_map(
            cls,
            data: List[str],
            search_header: str,
    ) -> Dict[range, Tuple[int, int]]:
        found_ranges = {}
        idx_found = data.index(search_header)
        for curr_idx in range(idx_found + 1, len(data)):
            curr_line = data[curr_idx]
            if curr_line == '':
                break
            dest_start, source_start, op_length = [
                int(x) for x in curr_line.split(' ')
            ]
            curr_range = range(source_start, source_start + op_length)
            found_ranges[curr_range] = (dest_start, op_length)
        return found_ranges

    @classmethod
    def _parse_maps(cls, data: List[str]):
        maps = {
            'seed-to-soil map:': None,
            'soil-to-fertilizer map:': None,
            'fertilizer-to-water map:': None,
            'water-to-light map:': None,
            'light-to-temperature map:': None,
            'temperature-to-humidity map:': None,
            'humidity-to-location map:': None,
        }

        for key_update in maps:
            found_map = cls._parse_map(data, key_update)
            maps[key_update] = found_map

        return maps

    @classmethod
    def _parse_seed_pairs(cls, data: List[str]) -> List[Tuple[int, int]]:
        seed_data = cls._parse_seeds(data)
        pairs = []
        for x, y in cls._pairwise(seed_data):
            pairs.append((x, y))
        return pairs

    @classmethod
    def _parse_seeds(cls, data: List[str]) -> List[int]:
        _, seeds_raw = data[0].split(':')
        return [int(x) for x in seeds_raw.split(' ') if len(x) > 0]

    @classmethod
    def _pairwise(cls, iterable):
        x = iter(iterable)
        return zip(x, x)

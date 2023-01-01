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

import itertools
from typing import (
    Dict,
    List,
)

from .paired_chars import PairedChars
from ..day_meta import DayMeta


class Day05(DayMeta):
    """
    Advent of Code 2015, Day 05
    """

    _bad_boys = {'ab', 'cd', 'pq', 'xy'}
    _vowels = {'a', 'e', 'i', 'o', 'u'}

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = Day05.get_lines_as_list_string('day_05.txt')

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
        results = 0

        for data_entry in data:
            if len(data_entry) < 3:
                continue

            has_bad_boys = False
            has_double = False
            has_vowels = False
            local_window = []
            vowel_count = 0

            for data_char in data_entry:
                # Only remove previous item if window full
                if len(local_window) == 2:
                    local_window.pop(0)
                # Always add the current item to the window
                local_window.append(data_char)

                # If this is a vowel, and we're counting. count
                if not has_vowels and data_char in cls._vowels:
                    vowel_count += 1
                    if vowel_count == 3:
                        has_vowels = True

                # We can only look at full windows.
                if len(local_window) < 2:
                    continue

                if len(set(local_window)) == 1 and not has_double:
                    has_double = True

                local_window_str = f'{local_window[0]}{local_window[1]}'
                if local_window_str in cls._bad_boys:
                    has_bad_boys = True
                    break

            if has_vowels and has_double and not has_bad_boys:
                results += 1

        return results

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 05.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        results = 0

        for data_entry in data:
            if len(data_entry) < 4:
                continue

            is_bridge_found = False
            is_pair_found = False
            bridge_window = []
            pairs_seen: Dict[str, List[PairedChars]] = {}

            for curr_idx, data_char in enumerate(data_entry):
                bridge_window.append(data_char)

                if not is_pair_found and curr_idx > 0:
                    local_pair = PairedChars(
                        data_entry[curr_idx - 1],
                        data_char,
                        curr_idx
                    )

                    pairs = pairs_seen.get(local_pair.str_pair, [])
                    pairs.append(local_pair)
                    pairs_seen[local_pair.str_pair] = pairs

                    for pair_a, pair_b in itertools.combinations(pairs, 2):
                        if not pair_a.overlaps(pair_b):
                            is_pair_found = True
                            break

                if not is_bridge_found and len(bridge_window) == 3:
                    is_bridged = bool(bridge_window[0] == bridge_window[2])
                    bridge_window.pop(0)
                    if is_bridged:
                        is_bridge_found = True

            if is_bridge_found and is_pair_found:
                results += 1

        return results

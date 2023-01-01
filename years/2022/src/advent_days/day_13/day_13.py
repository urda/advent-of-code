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

import ast
import functools
from copy import deepcopy
from typing import (
    Any,
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day13(DayMeta):
    """
    Advent of Code 2022, Day 13
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_13.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 13.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        parsed = cls._parse(data)

        good_signals = []

        for idx, signals in enumerate(parsed):
            result = cls._check_signals(*signals)
            if result != 1:
                good_signals.append(idx + 1)

        return sum(good_signals)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 13.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        divider_a: list[Any] = [[2]]
        divider_b: list[Any] = [[6]]
        signals = [divider_a, divider_b]

        for parsed_signal in cls._parse(data):
            for signal in parsed_signal:
                signals.append(signal)
        signals = sorted(signals, key=functools.cmp_to_key(cls._check_signals))

        return (signals.index(divider_a) + 1) * (signals.index(divider_b) + 1)

    @classmethod
    def _check_signals(
            cls,
            local_signal_left: List[int | list],
            local_signal_right: List[int | list],
    ) -> int:
        signal_left = deepcopy(local_signal_left)
        signal_right = deepcopy(local_signal_right)

        while len(signal_left) > 0 or len(signal_right) > 0:
            # Boundary Checks
            if len(signal_left) == 0 and len(signal_right) > 0:
                return -1
            if len(signal_left) > 0 and len(signal_right) == 0:
                return 1

            curr_left = signal_left.pop(0)
            curr_right = signal_right.pop(0)

            # If both are ints, perform direct compares
            if isinstance(curr_left, int) and isinstance(curr_right, int):
                possible_result = cls._check_signal_int(curr_left, curr_right)
                if possible_result != 0:
                    return possible_result
                continue

            # If not, someone needs to be "re-boxed"
            if isinstance(curr_left, int):
                curr_left = [curr_left]
            if isinstance(curr_right, int):
                curr_right = [curr_right]

            # We then call into the same function again, trying again.
            possible_result = cls._check_signals(curr_left, curr_right)
            if possible_result is not None:
                return possible_result

        return 0

    @classmethod
    def _check_signal_int(cls, left: int, right: int) -> int:
        if left < right:
            return -1
        if left > right:
            return 1
        return 0

    @classmethod
    def _parse(
            cls,
            data: List[str]
    ) -> List[Tuple[List[List[int]], List[List[int]]]]:
        data_size = len(data)
        scanner_ptr = 0
        step_size = 3

        results = []

        while scanner_ptr < data_size:
            packet_left = data[scanner_ptr]
            packet_right = data[scanner_ptr + 1]

            data_left = cls._parse_packet(packet_left)
            data_right = cls._parse_packet(packet_right)

            results.append((data_left, data_right))

            scanner_ptr += step_size

        return results

    @classmethod
    def _parse_packet(cls, raw_packet: str) -> List[List[int]]:
        results = []
        for data_entry in ast.literal_eval(raw_packet):
            results.append(data_entry)
        return results

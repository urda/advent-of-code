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
    Tuple,
)

from .instruction import Instruction
from .operation import Operation
from ..day_meta import DayMeta


class Day10(DayMeta):
    """
    Advent of Code 2022, Day 10
    """

    _check_cycles = {20, 60, 100, 140, 180, 220}
    _cycle_limit = 240
    _line_count_limit = 6
    _line_limit = 40

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_10.txt')

        results = [str(cls.compute_part_1(raw_data))]

        for data_line in cls.compute_part_2(raw_data):
            results.append(data_line)

        return results

    @classmethod
    def compute_part_1(cls, data: List[str]):
        """
        Parse the data and compute for Day 10.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._simulate_clock(cls._parse_instructions(data))

    @classmethod
    def compute_part_2(cls, data: List[str]) -> List[str]:
        """
        Parse the data and compute for Day 10.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._simulate_clock_crt(cls._parse_instructions(data))

    @classmethod
    def _build_pixel(cls, pixel_idx: int) -> Tuple[int, int, int]:
        return pixel_idx - 1, pixel_idx, pixel_idx + 1

    @classmethod
    def _parse_instructions(cls, data: List[str]) -> List[Instruction]:
        results = []
        for raw_instruction in data:
            if ' ' in raw_instruction:
                raw_op, raw_data = raw_instruction.split(' ', maxsplit=1)
            else:
                raw_op, raw_data = raw_instruction, None

            operation = Operation.convert_to_op(raw_op)
            match operation:
                case Operation.NOOP:
                    data = None
                case Operation.ADDX:
                    data = int(raw_data)

                    # Insert "noop" +0 instruction to deal with cycle count
                    for _ in range(operation.cycle_count - 1):
                        results.append(Instruction(operation, 0))

            results.append(Instruction(operation, data))

        return results

    @classmethod
    def _simulate_clock(cls, instructions: List[Instruction]) -> int:
        clock_signal = 1
        register_x = 1
        result = 0

        while clock_signal <= cls._cycle_limit:
            curr_instruction = instructions.pop(0)

            if clock_signal in cls._check_cycles:
                result += clock_signal * register_x

            match curr_instruction.operation:
                case Operation.NOOP:
                    pass
                case Operation.ADDX:
                    data = curr_instruction.data
                    register_x += data

            clock_signal += 1

        return result

    @classmethod
    def _simulate_clock_crt(cls, instructions: List[Instruction]) -> List[str]:
        results = []
        curr_line: List[str] = []

        clock_signal = 1
        register_x = 1

        while clock_signal <= cls._cycle_limit:
            curr_instruction = instructions.pop(0)

            if (clock_signal - 1) % 40 in cls._build_pixel(register_x):
                curr_line += '#'
            else:
                curr_line += '.'

            if len(curr_line) == 40:
                results.append(''.join(curr_line))
                curr_line = []

            match curr_instruction.operation:
                case Operation.NOOP:
                    pass
                case Operation.ADDX:
                    data = curr_instruction.data
                    register_x += data

            clock_signal += 1

        return results

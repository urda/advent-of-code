"""
Copyright 2025 Peter Urda

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

import re
from typing import List

import math

from ..day_meta import DayMeta


class Day06(DayMeta):
    """
    Advent of Code 2025, Day 06
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_06.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 06.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        # Tokenize each row via whitespace
        rows = [re.findall(r"\S+", line) for line in data]
        # Transpose rows -> columns
        columns = list(zip(*rows))

        result = 0
        for column in columns:
            operation = column[-1]
            numerics = list(map(int, column[:-1]))

            match operation:
                case '+':
                    result += sum(numerics)
                case '*':
                    result += math.prod(numerics)
                case _:
                    raise ValueError(f'Invalid operation: {operation}')

        return result

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 06.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        # Keep spacing
        width = max(len(line) for line in data)
        # Pad each line with spaces so all lines share width
        grid = [line.ljust(width) for line in data]

        operands: list[int] = []
        op = None
        result = 0

        for column in reversed(list(zip(*grid))):
            # if the whole column is spaces
            if all(char == ' ' for char in column):
                # and we have pending numbers
                if operands:
                    # Apply the stored operator and save the result
                    result += sum(operands) if op == '+' \
                        else math.prod(operands)
                    # Reset for the next group
                    operands, op = [], None
                continue
            # Build numbers from all but the last row of column
            num_str = ''.join(column[:-1]).strip()
            if num_str:
                operands.append(int(num_str))
            if column[-1] in '+*':
                op = column[-1]

        # Any remaining operands?
        if operands:
            result += sum(operands) if op == '+' else math.prod(operands)

        return result

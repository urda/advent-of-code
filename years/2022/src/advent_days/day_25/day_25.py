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

from typing import List

from ..day_meta import DayMeta


# pylint: disable=invalid-name
class Day25(DayMeta):
    """
    Advent of Code 2022, Day 25
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_25.txt')

        return [
            cls.compute_part_1(raw_data),
        ]

    @classmethod
    def compute_part_1(cls, data) -> str:
        """
        Parse the data and compute for Day 25.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._encode(sum(map(cls._decode, data)))

    @classmethod
    def _decode(cls, n):
        out = 0
        for d in n:
            out *= 5
            match d:
                case '2':
                    out += 2
                case '1':
                    out += 1
                case '-':
                    out -= 1
                case '=':
                    out -= 2
        return out

    @classmethod
    def _encode(cls, n):
        out = []
        while n:
            d = n % 5
            match d:
                case 0:
                    out.append('0')
                case 1:
                    out.append('1')
                case 2:
                    out.append('2')
                case 3:
                    out.append('=')
                    n += 2
                case 4:
                    out.append('-')
                    n += 1
            n //= 5
        return ''.join(reversed(out))

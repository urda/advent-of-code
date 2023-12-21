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
from itertools import repeat
from typing import (
    Dict,
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day16(DayMeta):
    """
    Advent of Code 2023, Day 16
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_16.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 16.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._energize_it([(-1, 1)], cls._parse(data))

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 16.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        parsed_data = cls._parse(data)
        return max(
            map(
                cls._energize_it,
                ([(pos - direction, direction)]
                 for direction in (1, 1j, -1, -1j)
                 for pos in parsed_data
                 if pos-direction not in parsed_data),
                repeat(parsed_data),
            )
        )

    @classmethod
    def _energize_it(
            cls,
            proc_queue: List[Tuple[complex, complex]],
            data: Dict[complex, str]
    ):
        done = set()
        while proc_queue:
            position, direction = proc_queue.pop()
            while not (position, direction) in done:
                done.add((position, direction))
                position += direction
                match data.get(position):
                    case '|':
                        direction = 1j
                        proc_queue.append((position, -direction))
                    case '-':
                        direction = -1
                        proc_queue.append((position, -direction))
                    case '/':
                        direction = -complex(direction.imag, direction.real)
                    case '\\':
                        direction = complex(direction.imag, direction.real)
                    case None:
                        break

        return len(set(pos for pos, _ in done)) - 1

    @classmethod
    def _parse(cls, data: List[str]) -> Dict[complex, str]:
        return {
            complex(i, j): char_val for j, data_row in enumerate(data)
            for i, char_val in enumerate(data_row)
        }

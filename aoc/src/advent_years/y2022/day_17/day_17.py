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

from .jet_pattern import JetPattern
from ..day_meta import DayMeta


class Day17(DayMeta):
    """
    Advent of Code 2022, Day 17
    """

    _rocks = (
        # Shape '-'
        (0, 1, 2, 3),
        # Shape '+'
        (1, 0 + 1j, 2 + 1j, 1 + 2j),
        # Shape '⅃'
        (0, 1, 2, 2 + 1j, 2 + 2j),
        # Shape '|'
        (0, 0 + 1j, 0 + 2j, 0 + 3j),
        # Shape '■'
        (0, 1, 0 + 1j, 1 + 1j),
    )

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_17.txt')[0]

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: str) -> int:
        """
        Parse the data and compute for Day 17.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls.drop_rocks(data, 2022)

    @classmethod
    def compute_part_2(cls, data) -> int:
        """
        Parse the data and compute for Day 17.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls.drop_rocks(data, 1e12)

    # pylint: disable=inconsistent-return-statements
    @classmethod
    def drop_rocks(cls, data: str, rock_count: int | float) -> int:
        """Drop those ROCKS"""
        # pylint: disable=too-many-locals

        jets = JetPattern(data).pattern
        grid, seen = set(), {}
        x_val = y_val = top = 0
        search_space = int(rock_count) + 1

        for step in range(search_space):
            curr_pos: complex = complex(2, top + 4)

            if step == rock_count:
                return int(top)

            coords = x_val, y_val
            if coords in seen:
                x_seen, y_seen = seen[coords]
                quotient, remainder = divmod(1e12 - step, step - x_seen)
                if remainder == 0:
                    if rock_count == 1e12:
                        return int(top + (top - y_seen) * quotient)
            else:
                seen[coords] = step, top

            rock = cls._rocks[x_val]
            x_val = (x_val + 1) % len(cls._rocks)

            while True:
                jet = jets[y_val]
                y_val = (y_val + 1) % len(jets)

                if cls._check_grid(curr_pos, jet.value, rock, grid):
                    # Move to SIDE
                    curr_pos += jet.value
                if cls._check_grid(curr_pos, -1j, rock, grid):
                    # Move DOWN
                    curr_pos += -1j
                else:
                    # CAN'T Move
                    break

            grid |= {curr_pos + r_value for r_value in rock}
            top = max(top, curr_pos.imag + [1, 0, 2, 2, 3][x_val])

    @classmethod
    def _check_grid(
            cls,
            position: complex,
            direction_value: complex,
            rock: Tuple[complex, ...],
            grid: Set[complex],
    ):
        return all(
            cls._is_empty(position + direction_value + r, grid) for r in rock
        )

    @classmethod
    def _is_empty(cls, position: complex, grid: Set[complex]):
        return position.real in range(7) \
            and position.imag > 0 \
            and position not in grid

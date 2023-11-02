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


class Day02(DayMeta):
    """
    Advent of Code 2022, Day 02
    """

    enemy_rock = 'A'
    enemy_paper = 'B'
    enemy_scissors = 'C'

    friendly_rock = 'X'
    friendly_paper = 'Y'
    friendly_scissors = 'Z'

    rocks = (enemy_rock, friendly_rock)
    papers = (enemy_paper, friendly_paper)
    scissors = (enemy_scissors, friendly_scissors)

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_02.txt')

        return [
            str(cls.parse_data(raw_data, 1)),
            str(cls.parse_data(raw_data, 2)),
        ]

    @classmethod
    def parse_data(cls, raw_data: List[str], parse_mode: int) -> int:
        """
        Parse the Day 02 data and convert into an understood format.

        :param raw_data: The raw data from Advent of Code
        :param parse_mode: The mode to parse this in
        :returns:
        """

        my_score = 0
        for data_entry in raw_data:
            enemy, friendly = data_entry.split(' ')

            match parse_mode:
                case 1:
                    my_score += cls.compute_part_1(enemy, friendly)
                case 2:
                    my_score += cls.compute_part_2(enemy, friendly)

        return my_score

    @classmethod
    def compute_part_1(cls, enemy, friendly) -> int:
        """
        Get Part 1's Answer
        """

        lost = 0
        draw = 3
        win = 6

        result = 0
        if friendly in cls.rocks:
            if enemy in cls.scissors:
                result += win + 1
            elif enemy in cls.papers:
                result += lost + 1
            else:
                result += draw + 1

        elif friendly in cls.papers:
            if enemy in cls.rocks:
                result += win + 2
            elif enemy in cls.scissors:
                result += lost + 2
            else:
                result += draw + 2

        else:
            if enemy in cls.papers:
                result += win + 3
            elif enemy in cls.rocks:
                result += lost + 3
            else:
                result += draw + 3

        return result

    @classmethod
    def compute_part_2(cls, enemy, friendly) -> int:
        """
        Get Part 2's Answer
        """

        lost = 0
        draw = 3
        win = 6

        result = 0
        if friendly == 'X':
            # we need to lose
            if enemy in cls.rocks:
                will_throw = 3
            elif enemy in cls.scissors:
                will_throw = 2
            else:
                will_throw = 1

            result += lost + will_throw
        elif friendly == 'Y':
            # we need to draw
            if enemy in cls.rocks:
                will_throw = 1
            elif enemy in cls.scissors:
                will_throw = 3
            else:
                will_throw = 2

            result += draw + will_throw
        else:
            # we need to win
            if enemy in cls.rocks:
                will_throw = 2
            elif enemy in cls.scissors:
                will_throw = 1
            else:
                will_throw = 3

            result += win + will_throw

        return result

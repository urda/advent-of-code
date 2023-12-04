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

from typing import List

from .cube_game_data import CubeGameData
from ..day_meta import DayMeta


class Day02(DayMeta):
    """
    Advent of Code 2023, Day 02
    """

    _colors = {
        'red': None,
        'green': None,
        'blue': None,
    }

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_02.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 02.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """

        search_limits = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }

        results = 0

        for data_line in data:
            game = cls._build_game(data_line)

            is_ok = True
            for color_name, max_value in search_limits.items():
                max_seen = game.games[color_name]
                if max_seen > max_value:
                    is_ok = False
                    break

            if is_ok:
                results += game.game_id

        return results

    @classmethod
    def compute_part_2(cls, data) -> int:
        """
        Parse the data and compute for Day 02.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        results = 0

        for data_line in data:
            game = cls._build_game(data_line)

            seens = 1
            for seen_value in game.games.values():
                seens = seens * seen_value
            results += seens

        return results

    @classmethod
    def _build_game(cls, raw_game_data: str) -> CubeGameData:
        game_id = int(raw_game_data.split(':')[0].split(' ')[1])
        return CubeGameData(game_id, cls._parse_games(raw_game_data))

    @classmethod
    def _parse_games(cls, data: str):
        results = {
            'red': 0,
            'blue': 0,
            'green': 0,
        }

        raw_games = data.split(':')[1].strip().split(';')
        for raw_game in raw_games:
            draws = raw_game.split(',')
            for draw in draws:
                draw_count, draw_name = draw.strip().split(' ')
                draw_int = int(draw_count)
                curr_int = results[draw_name]
                if draw_int > curr_int:
                    results[draw_name] = draw_int

        return results

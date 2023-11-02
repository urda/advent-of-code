"""
Copyright 2021 Peter Urda

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

from .day_meta import DayMeta


class Day21(DayMeta):
    """
    Advent Day 21
    """

    _data_file = 'day_21.txt'

    _board_size = 10
    _d100 = 100
    _delimiter = ':'
    _die_100_last_roll = 100
    _win_score = 1000

    @classmethod
    def get_player_positions(cls, raw_input: List[str]) -> Tuple[int, int]:
        """
        Extract player positions from input.

        :param raw_input: Raw input to process.
        :return: Player positions as a tuple: (Player 1, Player 2).
        """

        player_1_pos = int(raw_input[0].split(cls._delimiter)[1])
        player_2_pos = int(raw_input[1].split(cls._delimiter)[1])
        return player_1_pos, player_2_pos

    @classmethod
    def play_game(cls, start_positions: Tuple[int, int]) -> int:
        """
        SHALL WE PLAY A GAME?

        :param start_positions: The player's start positions.
        :return: the score of the losing player * number of die rolls
        """

        player_1_pos, player_2_pos = start_positions
        roll_counter = 0
        player_1_score = 0
        player_2_score = 0
        player_1_turn = True
        playing = True
        result = -1

        while playing:
            rolls = cls.roll_deterministic_d100() \
                    + cls.roll_deterministic_d100() \
                    + cls.roll_deterministic_d100()
            roll_counter += 3

            match player_1_turn:
                case True:
                    player_1_pos = cls.update_player_position(player_1_pos,
                                                              rolls)
                    player_1_score += player_1_pos

                    if player_1_score >= cls._win_score:
                        result = player_2_score * roll_counter
                        playing = False
                case False:
                    player_2_pos = cls.update_player_position(player_2_pos,
                                                              rolls)
                    player_2_score += player_2_pos

                    if player_2_score >= cls._win_score:
                        result = player_1_score * roll_counter
                        playing = False

            player_1_turn = not player_1_turn

        return result

    @classmethod
    def update_player_position(cls, player_pos: int, rolls: int) -> int:
        """
        Given a player position, and distance rolled, update it.

        :param player_pos: The current player position.
        :param rolls: The rolled distance.
        :return: The new player's position on the board.
        """
        player_pos += rolls
        if player_pos > cls._board_size:
            player_pos = player_pos % cls._board_size
            if player_pos == 0:
                player_pos = cls._board_size
        return player_pos

    @classmethod
    def roll_deterministic_d100(cls, reset_die: bool = False) -> int:
        """
        Perform a deterministic D100 die roll

        :param reset_die: Set to 'True' if you need the die to reset.
        :return: The die roll result.
        """

        # Should the die be reset?
        if reset_die:
            cls._die_100_last_roll = cls._d100
        # Roll die
        cls._die_100_last_roll += 1
        # If beyond threshold, roll back to 1
        if cls._die_100_last_roll == cls._d100 + 1:
            cls._die_100_last_roll = 1
        # Return deterministic die roll
        return cls._die_100_last_roll

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_game_input = cls.get_lines_as_list_string(cls._data_file)
        game_input = cls.get_player_positions(raw_game_input)
        part_1_result = cls.play_game(game_input)

        return [
            'Part 1:',
            f'Determined: {part_1_result}',
        ]

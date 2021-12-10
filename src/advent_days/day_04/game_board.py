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
    Dict,
    List,
    Optional,
    Tuple,
)

from .game_cell import GameCell


class GameBoard:
    """
    Game board for the Advent Day 04 work
    """

    _board_fixed_solution_size: int = 5
    _last_drawn_value: int = None
    _total_drawn_values: int = 0

    _game_cells: Dict[int, GameCell]
    _game_columns: Dict[int, list[GameCell]]
    _game_rows: Dict[int, list[GameCell]]

    def __init__(self, board_data: List[List[int]]):
        self._game_cells = {}
        self._game_columns = {}
        self._game_rows = {}

        for idx in range(self._board_fixed_solution_size):
            self._game_columns[idx] = []
            self._game_rows[idx] = []

        for row_idx, row in enumerate(board_data):
            for column_idx, cell_value in enumerate(row):
                game_cell = GameCell(cell_value)

                self._game_cells[cell_value] = game_cell
                self._game_columns[column_idx].append(game_cell)
                self._game_rows[row_idx].append(game_cell)

    def _compute_unmarked_sum(self) -> int:
        result = 0
        for cell in self._game_cells.values():
            if not cell.has_been_drawn:
                result += cell.cell_value
        return result

    def _discover_solution(self) -> Optional[Tuple[int, int]]:
        """
        Attempt to discover a solution in the board. Returns a tuple of
        result information, None if there are no solutions.

        :return: A tuple of the solution's unmarked sum, and the last
                 drawn value. Returns 'None' otherwise.
        """
        result = None
        search_space = \
            list(self._game_columns.values()) + list(self._game_rows.values())

        for cell_group in search_space:
            truthiness = True
            for cell in cell_group:
                truthiness = truthiness and cell.has_been_drawn
            if truthiness:
                result = self._compute_unmarked_sum(), self._last_drawn_value
                break

        return result

    def report_drawn_value(
            self,
            drawn_value: int
    ) -> Optional[Tuple[int, int]]:
        """
        Report a drawn value to the game board. Returns a tuple of solution
        information if a winner is found. None otherwise.

        :param drawn_value: The value you have drawn for BINGO.
        :return: None if no winner,
                 Tuple of (unmarked sum, value drawn) for winner.
        """
        self._last_drawn_value = drawn_value
        self._total_drawn_values += 1

        if drawn_value in self._game_cells:
            self._game_cells[drawn_value].has_been_drawn = True

        if self._total_drawn_values < self._board_fixed_solution_size:
            return None

        return self._discover_solution()

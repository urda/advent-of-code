from typing import (
    Dict,
    List,
    Optional,
    Tuple,
)

from .game_cell import GameCell


class GameBoard:
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

    def report_drawn_value(self, drawn_value: int):
        self._last_drawn_value = drawn_value
        self._total_drawn_values += 1

        if drawn_value in self._game_cells:
            self._game_cells[drawn_value].has_been_drawn = True

        if self._total_drawn_values < self._board_fixed_solution_size:
            return None
        else:
            return self._discover_solution()

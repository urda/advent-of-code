from dataclasses import dataclass


@dataclass
class GameCell:
    cell_value: int
    has_been_drawn: bool = False

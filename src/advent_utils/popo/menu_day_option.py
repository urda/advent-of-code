from dataclasses import (
    dataclass,
    field,
)
from typing import Callable


@dataclass
class MenuDayOption:
    day_id: int
    day_func: Callable

    menu_entry_title: str = field(init=False)

    def __post_init__(self):
        self.menu_entry_title = f'Day {self.day_id:02}'

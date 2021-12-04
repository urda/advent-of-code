from dataclasses import (
    dataclass,
    field,
)

from advent_days.days.day_meta import DayMeta


@dataclass
class MenuDayOption:
    day_id: int
    day_object: DayMeta.__subclasses__()

    menu_entry_title: str = field(init=False)

    def __post_init__(self):
        self.menu_entry_title = f'Day {self.day_id:02}'

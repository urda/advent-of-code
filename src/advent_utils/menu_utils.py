from typing import (
    Dict,
    List,
)

from advent_days.day_meta import DayMeta
from .popo import MenuDayOption


def build_menu_lookups(menu_data: List[MenuDayOption]) -> Dict[int, DayMeta]:
    results = {}
    for menu_entry in menu_data:
        results[menu_entry.day_id] = menu_entry.day_object
    return results


def print_menu(menu_data: List[MenuDayOption]):
    line_br = '-' * 80
    available_days = len(menu_data)

    print(line_br)
    print()
    print(f'Enter an advent day 1-{available_days}, or enter "0" to quit:')
    print()

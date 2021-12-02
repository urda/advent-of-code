from typing import (
    Callable,
    Dict,
    List,
)

from .popo import MenuDayOption


def build_menu_lookups(menu_data: List[MenuDayOption]) -> Dict[int, Callable]:
    results = {}
    for menu_entry in menu_data:
        results[menu_entry.day_id] = menu_entry.day_func
    return results


def print_menu(menu_data: List[MenuDayOption]):
    line_br = '-' * 80

    print(line_br)
    print()
    print('Pick an advent day from below, or enter "0" to quit:')
    print()
    for menu_entry in menu_data:
        print(menu_entry.menu_entry_title)
    print()

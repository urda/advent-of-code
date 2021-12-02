#!/usr/bin/env python3

from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
    Dict,
    List,
)

from advent_days.day_01.day_01 import Day01
from advent_days.day_02.day_02 import Day02


@dataclass()
class MenuDayOption:
    day_id: int
    day_func: Callable

    menu_entry_title: str = field(init=False)

    def __post_init__(self):
        self.menu_entry_title = f'Day {self.day_id:02}'


menu_options = [
    MenuDayOption(1, Day01.measure_depth),
    MenuDayOption(2, Day02.drive_sub),
]


def build_lookups(menu_data: List[MenuDayOption]) -> Dict[int, Callable]:
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


if __name__ == '__main__':
    running = True
    lookups = build_lookups(menu_options)

    while running:
        print_menu(menu_options)

        menu_option_raw_input = input('Enter day selection: ')
        if menu_option_raw_input.isdigit():
            menu_option_parsed = int(menu_option_raw_input)
        else:
            menu_option_parsed = None

        if menu_option_parsed in lookups:
            lookups.get(menu_option_parsed)()
        elif menu_option_parsed == 0:
            print('OK Thanks!')
            running = False
        else:
            print('Input not understood. Try again.')

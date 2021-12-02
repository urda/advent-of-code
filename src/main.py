#!/usr/bin/env python3

from advent_days import (
    Day01,
    Day02,
)
from advent_utils.menu_utils import (
    build_menu_lookups,
    print_menu,
)
from advent_utils.popo import MenuDayOption

menu_options = [
    MenuDayOption(1, Day01.measure_depth),
    MenuDayOption(2, Day02.drive_sub),
]


if __name__ == '__main__':
    running = True
    lookups = build_menu_lookups(menu_options)

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

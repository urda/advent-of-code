#!/usr/bin/env python3

from advent_days import (
    Day01,
    Day02,
    Day03,
    Day04,
    Day05,
    Day06,
)
from advent_utils.menu_utils import (
    build_menu_lookups,
    print_menu,
)
from advent_utils.popo import MenuDayOption

menu_options = [
    MenuDayOption(1, Day01),
    MenuDayOption(2, Day02),
    MenuDayOption(3, Day03),
    MenuDayOption(4, Day04),
    MenuDayOption(5, Day05),
    MenuDayOption(6, Day06),
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
            lookups.get(menu_option_parsed).solve_day_and_print()
        elif menu_option_parsed == 0:
            print()
            print('OK Bye Bye!')
            print()
            running = False
        else:
            print('Input not understood. Try again.')

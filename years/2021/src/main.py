#!/usr/bin/env python3
"""
The entry point for the ADVENT OF CODE!
"""

from advent_days import (
    Day01,
    Day02,
    Day03,
    Day04,
    Day05,
    Day06,
    Day07,
    Day08,
    Day09,
    Day10,
    Day21,
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
    MenuDayOption(7, Day07),
    MenuDayOption(8, Day08),
    MenuDayOption(9, Day09),
    MenuDayOption(10, Day10),
    MenuDayOption(21, Day21),
]


if __name__ == '__main__':
    lookups = build_menu_lookups(menu_options)

    while True:
        print_menu()

        menu_option_raw_input = input('Enter day selection: ')

        menu_option_parsed = int(menu_option_raw_input) \
            if menu_option_raw_input.isdigit() \
            else None

        if menu_option_parsed in lookups:
            lookups.get(menu_option_parsed).solve_day_and_print()
        elif menu_option_parsed == 0:
            print()
            print('OK Bye Bye!')
            print()
            break
        else:
            print('Input not understood. Try again.')
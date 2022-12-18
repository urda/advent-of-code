#!/usr/bin/env python3
"""
Copyright 2021-2022 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

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
    Day11,
    Day12,
    Day13,
    Day14,
    Day15,
    Day16,
    Day17,
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
    MenuDayOption(11, Day11),
    MenuDayOption(12, Day12),
    MenuDayOption(13, Day13),
    MenuDayOption(14, Day14),
    MenuDayOption(15, Day15),
    MenuDayOption(16, Day16),
    MenuDayOption(17, Day17),
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

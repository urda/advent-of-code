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

from advent_days.day_01 import (
    Day01,
)
from advent_utils.menu_utils import (
    build_menu_lookups,
    print_menu,
)
from advent_utils.popo import MenuDayOption

menu_options = [
    MenuDayOption(1, Day01),
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

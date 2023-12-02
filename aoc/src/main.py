#!/usr/bin/env python3
"""
Copyright 2021-2023 Peter Urda

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

from advent_utils.menu_utils import (
    build_menu_lookups,
    print_day_prompt,
    print_exit,
    print_year_prompt,
)
from menu import Menu


if __name__ == '__main__':
    menu_options = Menu.menu_entries

    lookups = build_menu_lookups(menu_options)
    year_option_parsed = print_year_prompt(list(menu_options.keys()))
    loaded_year = lookups.get(year_option_parsed)

    while True:
        menu_option_parsed = print_day_prompt()

        if menu_option_parsed in loaded_year:
            loaded_year.get(menu_option_parsed).solve_day_and_print()
        elif menu_option_parsed == 0:
            print_exit()
        else:
            print('Input not understood. Try again.')

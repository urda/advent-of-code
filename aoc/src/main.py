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
from advent_utils.popo import MenuDayOption
from advent_years import (
    y2015,
    y2021,
    y2022,
)

menu_options = {
    2015: [
        MenuDayOption(1, y2015.Day01),
        MenuDayOption(2, y2015.Day02),
        MenuDayOption(3, y2015.Day03),
        MenuDayOption(4, y2015.Day04),
        MenuDayOption(5, y2015.Day05),
        MenuDayOption(6, y2015.Day06),
        MenuDayOption(7, y2015.Day07),
        MenuDayOption(8, y2015.Day08),
        MenuDayOption(9, y2015.Day09),
        MenuDayOption(10, y2015.Day10),
        MenuDayOption(11, y2015.Day11),
        MenuDayOption(12, y2015.Day12),
        MenuDayOption(13, y2015.Day13),
        MenuDayOption(14, y2015.Day14),
        MenuDayOption(15, y2015.Day15),
        MenuDayOption(16, y2015.Day16),
        MenuDayOption(17, y2015.Day17),
    ],
    2021: [
        MenuDayOption(1, y2021.Day01),
        MenuDayOption(2, y2021.Day02),
        MenuDayOption(3, y2021.Day03),
        MenuDayOption(4, y2021.Day04),
        MenuDayOption(5, y2021.Day05),
        MenuDayOption(6, y2021.Day06),
        MenuDayOption(7, y2021.Day07),
        MenuDayOption(8, y2021.Day08),
        MenuDayOption(9, y2021.Day09),
        MenuDayOption(10, y2021.Day10),
        MenuDayOption(21, y2021.Day21),
    ],
    2022: [
        MenuDayOption(1, y2022.Day01),
        MenuDayOption(2, y2022.Day02),
        MenuDayOption(3, y2022.Day03),
        MenuDayOption(4, y2022.Day04),
        MenuDayOption(5, y2022.Day05),
        MenuDayOption(6, y2022.Day06),
        MenuDayOption(7, y2022.Day07),
        MenuDayOption(8, y2022.Day08),
        MenuDayOption(9, y2022.Day09),
        MenuDayOption(10, y2022.Day10),
        MenuDayOption(11, y2022.Day11),
        MenuDayOption(12, y2022.Day12),
        MenuDayOption(13, y2022.Day13),
        MenuDayOption(14, y2022.Day14),
        MenuDayOption(15, y2022.Day15),
        MenuDayOption(16, y2022.Day16),
        MenuDayOption(17, y2022.Day17),
        MenuDayOption(18, y2022.Day18),
        MenuDayOption(19, y2022.Day19),
        MenuDayOption(20, y2022.Day20),
        MenuDayOption(21, y2022.Day21),
        MenuDayOption(22, y2022.Day22),
        MenuDayOption(23, y2022.Day23),
        MenuDayOption(24, y2022.Day24),
        MenuDayOption(25, y2022.Day25),
    ]
}


if __name__ == '__main__':
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

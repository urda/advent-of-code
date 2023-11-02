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
"""
import sys
from typing import (
    Dict,
    List,
)

from advent_years.day_base import DayBase
from .popo import MenuDayOption


def build_menu_lookups(
        menu_data: Dict[int, List[MenuDayOption]]
) -> Dict[int, Dict[int, DayBase]]:
    """
    Give a dictionary of [YEAR -> [Advent Days]], build a dictionary that keys
    years and days to themselves for rapid lookup.

    :param menu_data: A dictionary of Years with MenuDayOption objects.
    :return: A dictionary of the objects keyed with their year and day.
    """
    results = {}

    for year_value, year_days in menu_data.items():
        loading_menu = {}
        for menu_entry in year_days:
            loading_menu[menu_entry.day_id] = menu_entry.day_object
        results[year_value] = loading_menu

    return results


def print_day_prompt() -> int:
    """
    Print prompt for day selection, return parsed day.
    """
    line_br = '-' * 80

    print(line_br)
    print()
    print('Enter an advent DAY number, or enter "0" to quit:')
    print()
    menu_option_raw_input = input('Enter day selection: ')

    return int(menu_option_raw_input) \
        if menu_option_raw_input.isdigit() else None


def print_exit() -> None:
    """
    Print exit prompt, and exit
    """
    print()
    print('OK Bye Bye!')
    print()
    sys.exit()


def print_year_prompt(supported_years: List[int]) -> int:
    """
    Print prompt for year selection, return supported year. Quit if sent '0'.
    """
    line_br = '-' * 80

    print(line_br)
    print('Supported years:')
    print()
    for supported_year in supported_years:
        print(f'● {supported_year}')

    while True:
        print(line_br)
        print()
        print('Enter an advent YEAR number, or enter "0" to quit:')
        print()
        year_option_raw_input = input('Enter year selection: ')

        year_option_parsed = int(year_option_raw_input) \
            if year_option_raw_input.isdigit() \
            else None

        if year_option_parsed in supported_years:
            return year_option_parsed

        if year_option_parsed == 0:
            print_exit()
        else:
            print('Year not supported. Try again.')

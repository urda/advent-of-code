"""
Copyright 2021 Peter Urda

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

from typing import (
    Dict,
    List,
)

from advent_days.day_meta import DayMeta
from .popo import MenuDayOption


def build_menu_lookups(menu_data: List[MenuDayOption]) -> Dict[int, DayMeta]:
    """
    Given a list of MenuDayOption objects, build a dictionary that keys their
    ID values to themselves.

    :param menu_data: A list of MenuDayOption objects.
    :return: A dictionary of the objects keyed with their ID.
    """
    results = {}
    for menu_entry in menu_data:
        results[menu_entry.day_id] = menu_entry.day_object
    return results


def print_menu(total_advent_days: int):
    """
    Given a list of MenuDayOption objects, using Python print display
    information about the

    :param total_advent_days:
    :return:
    """
    line_br = '-' * 80

    print(line_br)
    print()
    print(f'Enter an advent day 1-{total_advent_days}, or enter "0" to quit:')
    print()

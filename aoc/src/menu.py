"""
Copyright 2025 Peter Urda

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

from dataclasses import dataclass

from advent_utils.popo import MenuDayOption
from advent_years import (
    y2025,
)


@dataclass(init=False, frozen=True)
class Menu:
    menu_entries = {
        2025: [
            MenuDayOption(1, y2025.Day01),
            MenuDayOption(2, y2025.Day02),
            MenuDayOption(3, y2025.Day03),
            MenuDayOption(4, y2025.Day04),
        ],
    }

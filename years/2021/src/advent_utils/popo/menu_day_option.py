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

from dataclasses import (
    dataclass,
    field,
)

from advent_days.day_meta import DayMeta


@dataclass
class MenuDayOption:
    """
    Dataclass to contain an advent day class, helps produce menu information.
    """

    day_id: int
    day_object: DayMeta.__subclasses__()

    menu_entry_title: str = field(init=False)

    def __post_init__(self):
        self.menu_entry_title = f'Day {self.day_id:02}'

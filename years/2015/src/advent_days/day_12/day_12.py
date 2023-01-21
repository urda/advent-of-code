"""
Copyright 2023 Peter Urda

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

import json
import re
from typing import (
    Any,
    List,
)

from ..day_meta import DayMeta


class Day12(DayMeta):
    """
    Advent of Code 2015, Day 12
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_12.txt')[0]

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: str) -> int:
        """
        Parse the data and compute for Day 12.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return sum(int(x) for x in re.findall(r'[+-]?\d+', data))

    @classmethod
    def compute_part_2(cls, data: str) -> int:
        """
        Parse the data and compute for Day 12.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._traverse_json(json.loads(data))

    @classmethod
    def _traverse_json(cls, data: Any) -> int:
        results = 0

        match data:
            case int():
                return data
            case str():
                return 0
            case list():
                for entry in data:
                    results += cls._traverse_json(entry)
            case dict():
                for value in data.values():
                    if value == 'red':
                        return 0
                    results += cls._traverse_json(value)

        return results

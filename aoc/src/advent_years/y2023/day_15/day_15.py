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
import re
from collections import (
    OrderedDict,
    defaultdict,
)
from typing import List

from ..day_meta import DayMeta


class Day15(DayMeta):
    """
    Advent of Code 2023, Day 15
    """

    _FOCAL = '='
    _DASH = '-'

    _SPLIT = f'{_FOCAL}|{_DASH}'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_string('day_15.txt').strip()

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: str) -> int:
        """
        Parse the data and compute for Day 15.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        results = 0
        for sub_str in data.split(','):
            results += cls._parse_str(sub_str)
        return results

    @classmethod
    def compute_part_2(cls, data: str) -> int:
        """
        Parse the data and compute for Day 15.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        result = 0
        boxes = defaultdict(OrderedDict)

        for sub_str in data.split(','):
            label, focal_str = re.split(cls._SPLIT, sub_str)
            target_box = cls._parse_str(label)
            box = boxes[target_box]
            if len(focal_str) > 0:
                focal = int(focal_str)
                box[label] = focal
            else:
                if label in box:
                    box.pop(label)

        for box_idx, box in boxes.items():
            if len(box) == 0:
                continue
            for lens_idx, lens in enumerate(box):
                result += (box_idx + 1) * (lens_idx + 1) * box[lens]

        return result

    @classmethod
    def _parse_str(cls, sub_str: str) -> int:
        current_value = 0

        for sub_str_char in sub_str:
            # Determine the ASCII code for the current character of the string.
            ascii_val = ord(sub_str_char.encode('ascii'))
            # Increase the current value by the ASCII code you just determined.
            current_value += ascii_val
            # Set the current value to itself multiplied by 17.
            current_value = current_value * 17
            # Set the current value to the remainder of dividing itself by 256.
            current_value = current_value % 256

        return current_value

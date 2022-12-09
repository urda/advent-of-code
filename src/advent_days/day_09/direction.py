"""
Copyright 2022 Peter Urda

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

from __future__ import annotations

from enum import Enum


class Direction(Enum):
    """
    Enum to describe the "direction" of movement.
    """
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    @classmethod
    def convert_to_direction(cls, dir_char: str) -> Direction:
        """
        Convert the data character into a direction.
        :param dir_char: The data character to convert.
        :return: The matching enum, or ValueError
        """
        match dir_char[0].upper():
            case 'U':
                return Direction.UP
            case 'R':
                return Direction.RIGHT
            case 'D':
                return Direction.DOWN
            case 'L':
                return Direction.LEFT
            case _:
                raise ValueError('Invalid conversion')

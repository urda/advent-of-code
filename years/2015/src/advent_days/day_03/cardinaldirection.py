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


class CardinalDirection(Enum):
    """
    Enum to describe the "direction" of movement.
    """
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

    @classmethod
    def convert_to_direction(cls, dir_char: str) -> CardinalDirection:
        """
        Convert the data character into a direction.
        :param dir_char: The data character to convert.
        :return: The matching enum, or ValueError
        """
        match dir_char:
            case '^':
                return CardinalDirection.NORTH
            case 'v':
                return CardinalDirection.SOUTH
            case '>':
                return CardinalDirection.EAST
            case '<':
                return CardinalDirection.WEST
            case _:
                raise ValueError('Invalid conversion')

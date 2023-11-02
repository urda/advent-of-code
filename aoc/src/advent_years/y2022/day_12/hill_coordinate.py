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

from typing import Tuple


class HillCoordinate:
    """
    Advanced Python object for an (x, y) coordinate on this hill.
    """

    _coords: Tuple[int, int]
    _elevation: int
    _elevation_char: str

    # pylint: disable=duplicate-code
    _elevation_lut = {
        'S': 1,
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        'E': 27,
    }

    def __init__(self, x_coord: int, y_coord: int, elevation_char: str):
        self._coords = (x_coord, y_coord)
        self._elevation_char = elevation_char

        self._elevation = self._get_char_elevation_value(
            self._elevation_char
        )

    @property
    def coords(self) -> Tuple[int, int]:
        """Returns a tuple for the (x, y) coordinates for this object."""
        return self._coords

    @property
    def elevation(self) -> int:
        """Gets the elevation integer value."""
        return self._elevation

    @property
    def elevation_char(self) -> str:
        """Gets the elevation character value."""
        return self._elevation_char

    @property
    def is_end_coord(self) -> bool:
        """Reports if this coordinate was the 'end' coordinate."""
        return self.elevation_char == 'E'

    @property
    def is_start_coord(self) -> bool:
        """Reports if this coordinate was the 'start' coordinate."""
        return self.elevation_char == 'S'

    def can_navigate_to(self, target: HillCoordinate) -> bool:
        """Reports if a target can be reached from this coordinate."""
        return self.elevation + 1 >= target.elevation

    @classmethod
    def _get_char_elevation_value(cls, char_val: str) -> int:
        if char_val not in cls._elevation_lut:
            raise ValueError
        return cls._elevation_lut[char_val]

    def __eq__(self, other) -> bool:
        return self.coords == other.coords \
            and self.elevation_char == other.elevation_char

    def __gt__(self, other: HillCoordinate) -> bool:
        return self.elevation > other.elevation

    def __hash__(self) -> hash:
        return hash((
            self.coords,
            self.elevation_char,
        ))

    def __str__(self) -> str:
        return f'HillCoordinate(' \
               f'coords:{self.coords}, ' \
               f'elevation_char: {self.elevation_char}' \
               f'elevation: {self.elevation}' \
               f')'

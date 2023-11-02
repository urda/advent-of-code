"""
Copyright 2022-2023 Peter Urda

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


class Coordinate:
    """
    Advanced Python object for an (x, y) coordinate.
    """

    _x: int
    _y: int

    def __init__(self, x_val: int, y_val: int):
        self._x = x_val
        self._y = y_val

    @property
    def x(self) -> int:
        # pylint: disable=invalid-name
        # pylint: disable=missing-function-docstring
        return self._x

    @property
    def y(self) -> int:
        # pylint: disable=invalid-name
        # pylint: disable=missing-function-docstring
        return self._y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f'Coordinate(x:{self.x}, y: {self.y})'

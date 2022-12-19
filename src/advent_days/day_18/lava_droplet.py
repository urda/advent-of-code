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

from typing import (
    Annotated,
    List,
    Tuple,
)


class LavaDroplet:
    """Python class for the lava droplets in 3D space."""

    _x_pos: int
    _y_pos: int
    _z_pos: int

    def __init__(self, x_pos: int, y_pos: int, z_pos: int):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._z_pos = z_pos

    @property
    def coordinates(self) -> Tuple[int, int, int]:
        """Helper property to generate a coordinate tuple."""
        return self._x_pos, self._y_pos, self._z_pos

    @staticmethod
    def build_neighborhood(
            x_pos: int,
            y_pos: int,
            z_pos: int,
    ) -> List[Annotated[Tuple[int, int, int], 6]]:
        """Helper function to build a 3D coordinate neighborhood."""
        return [
            (x_pos - 1, y_pos, z_pos),
            (x_pos + 1, y_pos, z_pos),
            (x_pos, y_pos - 1, z_pos),
            (x_pos, y_pos + 1, z_pos),
            (x_pos, y_pos, z_pos - 1),
            (x_pos, y_pos, z_pos + 1),
        ]

    def __hash__(self) -> hash:
        return hash((
            self._x_pos,
            self._y_pos,
            self._z_pos,
        ))

    def __str__(self) -> str:
        return f'{type(self).__name__}(' \
               f'x={self._x_pos}, ' \
               f'y={self._y_pos}, ' \
               f'z={self._z_pos}' \
               f')'

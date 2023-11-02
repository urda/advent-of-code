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

from .direction import Direction


class Movement:
    """
    This class models a "movement" from the data file.
    """
    _direction: Direction
    _steps: int

    def __init__(self, movement: str):
        raw_direction, raw_steps = movement.split(' ')
        self._direction = Direction.convert_to_direction(raw_direction)
        self._steps = int(raw_steps)

    @property
    def direction(self) -> Direction:
        # pylint: disable=missing-function-docstring
        return self._direction

    @property
    def steps(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._steps

    def __str__(self) -> str:
        return f'Movement({self.direction} :: {self.steps})'

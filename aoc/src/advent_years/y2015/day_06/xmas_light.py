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


class XmasLight:
    """A pretty Christmas light."""
    _on: bool
    _pos_x: int
    _pos_y: int

    def __init__(self, pos_x: int, pos_y: int):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._on = False

    @property
    def on(self) -> bool:
        """Read the current state of the light."""
        # pylint: disable=invalid-name
        return self._on

    @on.setter
    def on(self, value: bool):
        """Directly control the light with 'on' state."""
        # pylint: disable=invalid-name
        self._on = value

    @property
    def pos_x(self) -> int:
        """The reported 'x' position on the grid for this light."""
        return self._pos_x

    @property
    def pos_y(self) -> int:
        """The reported 'y' position on the grid for this light."""
        return self._pos_y

    def toggle(self):
        """Toggle this light's state."""
        # pylint: disable=invalid-name
        self.on = not self.on

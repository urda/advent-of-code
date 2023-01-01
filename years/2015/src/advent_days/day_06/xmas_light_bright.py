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

from .xmas_light import XmasLight


class XmasLightBright(XmasLight):
    """A pretty Christmas light, with brightness levels."""
    _brightness: int

    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(pos_x, pos_y)
        self._brightness = 0

    @property
    def brightness(self) -> int:
        """Get the reported 'brightness' of this light."""
        return self._brightness

    @property
    def on(self) -> bool:
        """Read the current state of the light."""
        return self.brightness > 0

    @on.setter
    def on(self, value: bool):
        raise NotImplementedError('Unsupported in this type.')

    def set_off(self):
        """Force the light off, makes it darker until 0."""
        self._brightness -= 1 if self.on else 0

    def set_on(self):
        """Force the light on, makes it brighter."""
        self._brightness += 1

    def toggle(self):
        self._brightness += 2

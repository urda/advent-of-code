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

from dataclasses import dataclass


@dataclass(init=False)
class DigPlanStep:
    """
    Given a raw dig plan string, create the Dig Plan Step python object.
    """

    _action_map = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U',
    }

    direction: str
    steps: int
    hex_color: str

    def __init__(self, raw_data: str, decode_hex: bool = False):
        self.direction, raw_steps, raw_color = raw_data.split(' ')
        self.steps = int(raw_steps)
        self.hex_color = raw_color[2:-1]

        if decode_hex:
            self.direction = self._action_map[self.hex_color[5]]
            self.steps = int(self.hex_color[:5], 16)

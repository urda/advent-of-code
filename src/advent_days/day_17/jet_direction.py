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


class JetDirection(Enum):
    """Enum for the LEFT / RIGHT direction and their values in grid."""

    LEFT = -1
    RIGHT = 1

    @staticmethod
    def parse_direction(direction_char: str) -> JetDirection:
        """Convert a given character to the actual enum."""
        match direction_char:
            case '>':
                return JetDirection.RIGHT
            case '<':
                return JetDirection.LEFT
            case _:
                raise ValueError

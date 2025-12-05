"""
Copyright 2025 Peter Urda

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


class SafeDial:
    """
    Python object to contain the dial and the dial state.
    """
    _starting_pos: int = 50
    _lower: int = 0
    _upper: int = 99

    _dir_left: str = 'L'
    _dir_right: str = 'R'
    _dirs: set[str] = (_dir_left, _dir_right)

    _actions: dict[str, int] = {
        _dir_left: -1,
        _dir_right: 1,
    }

    _dir_pos: int = _starting_pos

    def __init__(self):
        pass

    def spin_dial(self, dial_input: str) -> int:
        """
        Spin the dial and return the position.
        """
        action, distance = self._get_spin_info(dial_input)
        self._dir_pos = (self._dir_pos + action * distance) % 100
        return self._dir_pos

    def spin_zero(self, dial_input: str) -> int:
        """
        Spin the dial, tracking the times we land or pass on zero.
        """
        action, distance = self._get_spin_info(dial_input)
        # steps until the first time we’d hit 0 going this direction
        first_hit = (-self._dir_pos * action) % 100
        if first_hit == 0:
            first_hit = 100  # don’t count starting on 0

        hits = 0 if distance < first_hit else 1 + (distance - first_hit) // 100

        # advance dial
        self._dir_pos = (self._dir_pos + action * distance) % 100
        return hits

    @classmethod
    def _get_spin_info(cls, dial_input: str) -> tuple[int, int]:
        raw_dir, raw_distance = dial_input[:1], dial_input[1:]
        return cls._actions[raw_dir], int(raw_distance)

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

from typing import List

from .pass_char import PassChar


class PassCharRoot(PassChar):
    """
    Smarter password character node.
    This is the "root", or most-far-right character in the string.
    It can handle incrementing the entire string,
    and reporting the full password. Has vision to all other character nodes.
    """

    _init_value: str
    _pass_length: int

    _neighborhood: List[PassChar]

    def __init__(self, init_value: str, pass_length: int):
        self._init_value = init_value
        self._pass_length = pass_length

        if len(self.init_value) != self.pass_length:
            raise ValueError(f'Password needs to be {self.pass_length}')

        super().__init__(self.init_value[-1], self._build_neighborhood())

    @property
    def init_value(self) -> str:
        """Reports the initial string used to build the chain."""
        return self._init_value

    @property
    def neighborhood(self) -> List[PassChar]:
        """Reports the neighborhood as the root node sees it."""
        return self._neighborhood

    @property
    def pass_length(self) -> int:
        """Gets the 'length' of this password character chain."""
        return self._pass_length

    def get_password(self) -> str:
        """Build the entire password as a string result."""
        return ''.join([char_ptr.value for char_ptr in self.neighborhood])

    def _build_neighborhood(self) -> PassChar:
        last_char = None
        neighbors = []

        for letter in [*self.init_value][:-1]:
            new_char = PassChar(letter, last_char)
            neighbors.append(new_char)
            last_char = new_char
        neighbors.append(self)

        self._neighborhood = neighbors
        return last_char

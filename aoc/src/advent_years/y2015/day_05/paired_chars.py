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


class PairedChars:
    """
    Models a "pair" of characters and their indexes
    """

    _idx_left: int
    _idx_right: int

    _left: str
    _right: str

    def __init__(self, left_char: str, right_char: str, right_idx: int):
        self._idx_left = right_idx - 1
        self._idx_right = right_idx
        self._left = left_char
        self._right = right_char

    @property
    def idx_left(self) -> int:
        """Get the left character's index value."""
        return self._idx_left

    @property
    def idx_right(self) -> int:
        """Get the right character's index value."""
        return self._idx_right

    @property
    def left(self) -> str:
        """Get the left character."""
        return self._left

    @property
    def right(self) -> str:
        """Get the right character."""
        return self._right

    @property
    def str_pair(self) -> str:
        """
        Get the string representation of just the paired characters.
        :return: The left and right as a two-character-string.
        """
        return f'{self.left}{self.right}'

    def overlaps(self, other: PairedChars) -> bool:
        """
        Determine if another PairedChars overlaps this one.
        :param other: The other pair to compare with.
        :return: 'True' if any overlap, 'False' otherwise.
        """
        return (self == other) \
            or (other.idx_right == self.idx_left) \
            or (self.idx_right == other.idx_left)

    def __eq__(self, other: PairedChars):
        chars_match = self.left == other.left and self.right == other.right
        left_idx_match = self.idx_left == other.idx_left
        right_idx_match = self.idx_right == other.idx_right
        return chars_match and left_idx_match and right_idx_match

    def __hash__(self):
        return hash((self.idx_left, self.left, self.idx_right, self.right))

    def __str__(self):
        return f'PairedChars(' \
               f'{self.left}@{self.idx_left} :: ' \
               f'{self.right}@{self.idx_right})'

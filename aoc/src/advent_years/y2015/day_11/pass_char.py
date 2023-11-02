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

from __future__ import annotations

from typing import (
    Optional,
    Union,
)
from .pass_luts import PassLuts


class PassChar:
    """Contains a single character of the password."""

    _value_int: int
    _next_char: PassChar

    _MIN_CHAR: str = 'a'
    _MAX_CHAR: str = 'z'
    _MIN_VALUE: int = 1
    _MAX_VALUE: int = 23

    def __init__(self, value: Union[int, str], next_char: PassChar = None):
        match value:
            case int():
                if value < self._MIN_VALUE or value > self._MAX_VALUE:
                    raise ValueError(f'Integer values must be '
                                     f'{self._MIN_VALUE}-{self._MAX_VALUE}.')
            case str():
                if len(value) != self._MIN_VALUE:
                    raise ValueError(f'Only length of '
                                     f'{self._MIN_VALUE} allowed.')

                value = PassLuts.lookup(value)
            case _:
                raise TypeError("'value' must be int or str.")

        self._value_int = value
        self._next_char = next_char

    @property
    def next_char(self) -> Optional[PassChar]:
        """Gets the next character in the chain, None otherwise."""
        return self._next_char

    @property
    def value(self) -> str:
        """Gets the current password character value."""
        return PassLuts.lookup(self.value_int)

    @property
    def value_int(self) -> int:
        """Gets the current value, as an integer."""
        return self._value_int

    def increment_value(self) -> None:
        """
        Increase the value of this character, including carry bits.
        """
        self._value_int += 1

        if self._value_int > self._MAX_VALUE:
            if self.next_char:
                self._value_int = self._MIN_VALUE
                self._next_char.increment_value()
            else:
                self._value_int = self._MAX_VALUE
                raise OverflowError('Password limit reached!')

    def __str__(self) -> str:
        return f"{type(self).__name__}(" \
               f"value='{self.value}'" \
               f")"

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

from advent_common.pointer import Pointer


class LinkedPointer(Pointer):
    """
    Advanced Python object for an (x, y) coordinate pointer, with a "next".
    """

    _next: LinkedPointer

    def __init__(self, x_val: int, y_val: int, next_ptr: LinkedPointer = None):
        super().__init__(x_val, y_val)

        self._next = next_ptr

    @property
    def next(self) -> LinkedPointer:
        # pylint: disable=missing-function-docstring
        return self._next

    @next.setter
    def next(self, next_val: LinkedPointer):
        self._next = next_val

    def __str__(self) -> str:
        local_next = self.next.coordinate if self.next else None
        return f'LinkedPointer(x:{self.x}, y: {self.y}, next: {local_next})'

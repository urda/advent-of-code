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


class Operation(Enum):
    """
    Models a given "operation" our CPU / clock can perform here.
    """
    NOOP = 0
    ADDX = 1

    @classmethod
    def convert_to_op(cls, raw_op: str) -> Operation:
        """
        Convert a raw operation into a real operation.

        :param raw_op: The data string to convert.
        :return: The matching enum, or ValueError
        """
        match raw_op.lower():
            case 'noop':
                return Operation.NOOP
            case 'addx':
                return Operation.ADDX
            case _:
                raise ValueError('Invalid conversion')

    @property
    def cycle_count(self) -> int:
        """
        Reports the known "cycles" needed for an operation.
        :return: The cycle count an operation needs to run.
        """
        match self:
            case Operation.NOOP:
                return 1
            case Operation.ADDX:
                return 2
            case _:
                raise ValueError

    def __str__(self):
        return f'Operation::{self.name}'

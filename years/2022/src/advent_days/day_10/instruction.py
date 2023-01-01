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

from typing import Any

from .operation import Operation


class Instruction:
    """
    Class to model a given instruction. An instruction is operation + data.
    """

    _operation: Operation
    _data: Any

    def __init__(self, operation: Operation, data: Any = None):
        self._operation = operation
        self._data = data

    @property
    def data(self) -> Any:
        """
        :return: The data associated with this instruction.
        """
        return self._data

    @property
    def operation(self) -> Operation:
        """
        :return: The operation this instruction needs to perform.
        """
        return self._operation

    def __str__(self):
        return f'Instruction(op: {self.operation}, data: {self.data})'

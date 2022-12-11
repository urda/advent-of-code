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

from typing import List


# pylint: disable=too-many-instance-attributes
# pylint: disable=missing-function-docstring
class RowdyMonkey:
    """This monkey is rowdy!"""

    _monkey_id: int

    _items: List[int]
    _operation: str
    _test_operation: str
    _test_target_pass: int
    _test_target_fail: int

    _divisor: int
    _inspections: int

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            monkey_id: int,
            starting_items: List[int],
            operation: str,
            test: str,
            test_true: str,
            test_false: str,
    ):
        if 'divisible by' not in test:
            raise ValueError('Unsupported test type')

        self._monkey_id = monkey_id

        self._items = starting_items
        self._operation = operation.split('new = ')[1]
        self._divisor = int(test.split('divisible by ')[1])
        self._test_operation = f'value % {self._divisor} == 0'

        self._test_target_pass = self._parse_throw_to(test_true)
        self._test_target_fail = self._parse_throw_to(test_false)

        self._inspections = 0

    @property
    def _key_throw_to(self) -> str:
        return 'throw to monkey'

    @property
    def divisor(self) -> int:
        return self._divisor

    @property
    def inspections(self) -> int:
        return self._inspections

    @inspections.setter
    def inspections(self, value: int):
        self._inspections = value

    @property
    def items(self) -> List[int]:
        return self._items

    @items.setter
    def items(self, value: List[int]):
        self._items = value

    @property
    def monkey_id(self) -> int:
        return self._monkey_id

    @property
    def operation(self) -> str:
        return self._operation

    @property
    def target_fail(self) -> int:
        return self._test_target_fail

    @property
    def target_pass(self) -> int:
        return self._test_target_pass

    @property
    def test_operation(self) -> str:
        return self._test_operation

    def get_throw_to(self, value: int) -> int:
        """
        For a given value, determine where it should be "thrown" to

        WARNING:
            TRUST, BUT VERIFY YOUR INPUTS.
            This contains an `eval()` operation!

        :param value: The value to test.
        :return: The target to throw to.
        """
        if self.perform_test(value):
            return self.target_pass

        return self.target_fail

    def perform_operation(self, value: int) -> int:
        """
        Perform the operation of this monkey.

        WARNING:
            TRUST, BUT VERIFY YOUR INPUTS.
            This contains an `eval()` operation!

        :param value: The value to process.
        :return: The result of the operation given the value.
        """
        operation = self.operation.replace('old', str(value))
        # pylint: disable=eval-used
        return eval(operation)

    def perform_test(self, value: int) -> bool:
        """
        Perform the test operation of this monkey.

        WARNING:
            TRUST, BUT VERIFY YOUR INPUTS.
            This contains an `eval()` operation!

        :param value: The value to test.
        :return: The result of the test given the value.
        """
        operation = self.test_operation.replace('value', str(value))
        # pylint: disable=eval-used
        return eval(operation)

    def _parse_throw_to(self, throw_str: str) -> int:
        return int(throw_str.split(self._key_throw_to)[1].strip())

    def __str__(self):
        return f'RowdyMonke(' \
               f'monkey_id=\'{self.monkey_id}\', ' \
               f'operation=\'{self.operation}\', ' \
               f'test_operation=\'{self.test_operation}\'' \
               f')'

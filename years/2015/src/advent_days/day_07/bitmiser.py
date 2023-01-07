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
from copy import deepcopy
from typing import Dict


class BitMiser:
    """
    They call me Bit Miser, whatever I touch, turns to code in my clutch.

    I'm too much.
    """

    # pylint: disable=too-few-public-methods

    _calculations: Dict[str, list]
    _results: Dict[str, int]

    def __init__(self, calculations: Dict[str, list]):
        self._calculations = deepcopy(calculations)
        self._results = {}

    def calculate(self, target: str) -> int:
        """
        Perform calculations with the current state of this object.
        """

        try:
            return int(target)
        except ValueError:
            pass

        if target not in self._results:
            ops = self._calculations[target]
            if len(ops) == 1:
                res = self.calculate(ops[0])
            else:
                operation = ops[-2]
                match operation:
                    case 'AND':
                        res = self.calculate(ops[0]) & self.calculate(ops[2])
                    case 'OR':
                        res = self.calculate(ops[0]) | self.calculate(ops[2])
                    case 'NOT':
                        res = ~self.calculate(ops[1]) & 0xffff
                    case 'RSHIFT':
                        res = self.calculate(ops[0]) >> self.calculate(ops[2])
                    case 'LSHIFT':
                        res = self.calculate(ops[0]) << self.calculate(ops[2])
                    case _:
                        raise TypeError('Operation not understood')
            self._results[target] = res
        return self._results[target]

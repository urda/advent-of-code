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

from .pulse_module import PulseModule


class ConjunctionModule(PulseModule):
    """
    Conjunction modules (prefix &)
    """

    counts = 0
    states = 0
    conn = 0
    linked = []

    def __init__(self, module_id, targets):
        super().__init__(module_id, targets)
        self.states = 0
        self.counts = 0
        self.conn = 0
        self.linked = []

    def add(self, second_id: int):
        self.linked.append(second_id)
        self.conn += 1

    def pulse(self, level: int, source: int):
        self.counts |= level << source
        self.states &= ~(1 << source)
        self.states |= (level << source)

        if self.states.bit_count() == self.conn:
            return super().pulse(0, source)
        return super().pulse(1, source)

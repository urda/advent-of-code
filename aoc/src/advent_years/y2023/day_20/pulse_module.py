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


class PulseModule:
    """
    Generic pulse module
    """

    module_id = None
    targets = None

    def __init__(self, module_id, targets):
        self.module_id = module_id
        self.targets = targets

    def add(self, second_id):
        """Allow modules to 'add'."""

    # pylint: disable=unused-argument
    def pulse(self, level: int, source: int):
        """Pulse the signal across modules"""
        return [
            (self.module_id, level, dest) for dest in self.targets
        ]

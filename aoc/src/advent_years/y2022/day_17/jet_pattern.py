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

from copy import deepcopy
from typing import List

from .jet_direction import JetDirection


# pylint: disable=too-few-public-methods
class JetPattern:
    """Container class for a collection of JetDirections"""

    _pattern: List[JetDirection]
    _raw_input: str

    def __init__(self, raw_input: str):
        self._raw_input = raw_input

        self._parse_pattern()

    @property
    def pattern(self):
        """Get deep copy of the pattern for this Jet pattern."""
        return deepcopy(self._pattern)

    def _parse_pattern(self):
        self._pattern = [
            JetDirection.parse_direction(value)
            for value in self._raw_input
        ]

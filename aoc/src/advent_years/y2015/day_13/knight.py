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

from typing import Dict


class Knight:
    """A Knight of the Dinner Table."""

    _name: str
    _relations: Dict[str, int]

    def __init__(self, name: str):
        self._name = name
        self._relations = {}

    @property
    def name(self) -> str:
        """Gets the name of this Knight."""
        return self._name

    @property
    def relations(self) -> Dict[str, int]:
        """Reports the known relations of this Knight."""
        return self._relations

    def get_relation(self, other_name: str) -> int:
        """Fetch a relation for a given name."""
        if other_name not in self._relations:
            raise ValueError(f"'{other_name}' is not registered.")

        return self._relations[other_name]

    def register_relation(self, other_name: str, happiness: int) -> None:
        """Register a new relation for a given name."""
        if other_name in self._relations:
            raise OverflowError(f"'{other_name}' is already registered.")

        self._relations[other_name] = happiness

    def __str__(self):
        return f"{type(self).__name__}(" \
               f"name='{self.name}'" \
               f")"

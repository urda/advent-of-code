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

from dataclasses import dataclass
from typing import Dict


@dataclass(init=True, frozen=True)
class SueData:
    """
    Frozen dataclass for a single Sue.
    """
    # pylint: disable=too-many-instance-attributes

    sue_id: int

    children: int = -1
    cats: int = -1
    samoyeds: int = -1
    pomeranians: int = -1
    akitas: int = -1
    vizslas: int = -1
    goldfish: int = -1
    trees: int = -1
    cars: int = -1
    perfumes: int = -1

    def __str__(self) -> str:
        return (f'Sue #{self.sue_id} ('
                f'children: {self.children}, '
                f'cats: {self.cats}, '
                f'samoyeds: {self.samoyeds}, '
                f'pomeranians: {self.pomeranians}, '
                f'akitas: {self.akitas}, '
                f'vizslas: {self.vizslas}, '
                f'goldfish: {self.goldfish}, '
                f'trees: {self.trees}, '
                f'cars: {self.cars}, '
                f'perfumes: {self.perfumes}'
                f')')

    def set_values_as_dict(self) -> Dict[str, int]:
        """
        Get only "set", or defined Sue datapoints as a dictionary.
        """
        del_keys = []
        values = self.values_as_dict()
        for key, value in values.items():
            if value < 0:
                del_keys.append(key)
        for key in del_keys:
            values.pop(key)
        return values

    def values_as_dict(self) -> Dict[str, int]:
        """
        Get all the Sue datapoints as a dictionary.
        """
        return {
            'children': self.children,
            'cats': self.cats,
            'samoyeds': self.samoyeds,
            'pomeranians': self.pomeranians,
            'akitas': self.akitas,
            'vizslas': self.vizslas,
            'goldfish': self.goldfish,
            'trees': self.trees,
            'cars': self.cars,
            'perfumes': self.perfumes,
        }

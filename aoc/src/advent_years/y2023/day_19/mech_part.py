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


@dataclass(init=False)
class MechPart:
    """
    Xmas Machine Part
    """

    part_vals: Dict[str, int]
    part_rating: int

    def __init__(self, raw_cats: str):
        self.part_vals = {}
        for raw_cat in raw_cats[:-1][1:].split(','):
            cat_id, cat_val = raw_cat.split('=')
            self.part_vals[cat_id] = int(cat_val)
        self.part_rating = (self.part_vals['x'] +
                            self.part_vals['m'] +
                            self.part_vals['a'] +
                            self.part_vals['s'])

    def __str__(self) -> str:
        return (f'MechPart('
                f'x={self.part_vals["x"]}, '
                f'm={self.part_vals["m"]}, '
                f'a={self.part_vals["a"]}, '
                f's={self.part_vals["s"]})')

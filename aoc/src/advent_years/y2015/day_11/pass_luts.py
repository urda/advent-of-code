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

from typing import (
    Dict,
    Union,
)


class PassLuts:
    """
    Single Class Ref for all password lookup values.
    """

    # pylint: disable=too-few-public-methods

    @classmethod
    def lookup(cls, value: Union[int, str]) -> Union[int, str]:
        """Lookup a given value in the LUT."""
        return cls._master_lut[value]

    # pylint: disable=duplicate-code
    _master_lut: Dict[Union[int, str], Union[int, str]] = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'j': 9,
        'k': 10,
        'm': 11,
        'n': 12,
        'p': 13,
        'q': 14,
        'r': 15,
        's': 16,
        't': 17,
        'u': 18,
        'v': 19,
        'w': 20,
        'x': 21,
        'y': 22,
        'z': 23,
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'j',
        10: 'k',
        11: 'm',
        12: 'n',
        13: 'p',
        14: 'q',
        15: 'r',
        16: 's',
        17: 't',
        18: 'u',
        19: 'v',
        20: 'w',
        21: 'x',
        22: 'y',
        23: 'z',
    }

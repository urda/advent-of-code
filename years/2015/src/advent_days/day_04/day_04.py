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

from hashlib import md5
from typing import List

from ..day_meta import DayMeta


class Day04(DayMeta):
    """
    Advent of Code 2015, Day 04
    """

    # noinspection SpellCheckingInspection
    _data = 'iwrupvqb'
    _search_limit = 1000000000

    @classmethod
    def solve_day(cls) -> List[str]:
        return [
            str(cls.compute_part_1(cls._data)),
            str(cls.compute_part_2(cls._data)),
        ]

    @classmethod
    def compute_part_1(cls, data) -> int:
        """
        Parse the data and compute for Day 04.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._search_space(data, '00000')

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 04.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._search_space(data, '000000')

    @classmethod
    def _hash_md5(cls, data_str: str, data_int: int) -> str:
        hash_str: bytes = f'{data_str}{data_int}'.encode('utf-8')
        return md5(hash_str).hexdigest()

    @classmethod
    def _search_space(cls, data_str: str, search_key: str) -> int:
        """
        Perform a restricted search to find the possible advent coin.

        :raises: RecursionError: If the search limit is reached, aborts.

        :param data_str: The data key to hash with.
        :param search_key: The search key the coin should start with.
        :return: The matching integer value to build that hash.
        """
        idx_val = 1

        while idx_val <= cls._search_limit:
            hashes = cls._hash_md5(data_str, idx_val).startswith(search_key)
            if hashes:
                return idx_val

            idx_val += 1

        raise RecursionError('Search halted')

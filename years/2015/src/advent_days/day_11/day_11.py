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

from typing import List

from .pass_char_root import PassCharRoot
from ..day_meta import DayMeta


class Day11(DayMeta):
    """
    Advent of Code 2015, Day 11
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_11.txt')[0]
        part_1_result = cls.compute_part(raw_data)
        part_2_result = cls.compute_part(part_1_result)

        return [
            part_1_result,
            part_2_result,
        ]

    @classmethod
    def compute_part(cls, data: str) -> str:
        """
        Parse the data and compute for Day 11.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1 or 2.
        """
        pass_length = 8
        password = PassCharRoot(data, pass_length=pass_length)

        # Force skip the provided password if already "valid".
        if cls._string_conforms(password):
            password.increment_value()

        while True:
            try:
                if cls._string_conforms(password):
                    return password.get_password()
                password.increment_value()
            except OverflowError as err:
                raise err

    @classmethod
    def _string_conforms(cls, root_node: PassCharRoot) -> bool:
        passes_pairs = cls._string_has_pairs(root_node)
        passes_trio = cls._string_has_trio(root_node)
        return passes_pairs and passes_trio

    @classmethod
    def _string_has_pairs(cls, root_node: PassCharRoot) -> bool:
        curr_ptr = 0
        last_ptr = root_node.pass_length - 1

        seen = set()
        while curr_ptr < last_ptr:
            char_id_a = root_node.neighborhood[curr_ptr].value_int
            char_id_b = root_node.neighborhood[curr_ptr + 1].value_int

            if char_id_a == char_id_b and char_id_a not in seen:
                seen.add(char_id_a)

                if len(seen) == 2:
                    return True

                curr_ptr += 2
            else:
                curr_ptr += 1

        return False

    @classmethod
    def _string_has_trio(cls, root_node: PassCharRoot) -> bool:
        curr_ptr = 0
        last_ptr = root_node.pass_length - 2

        while curr_ptr < last_ptr:
            lookup_list: List[int] = [
                root_node.neighborhood[curr_ptr].value_int,
                root_node.neighborhood[curr_ptr + 1].value_int,
                root_node.neighborhood[curr_ptr + 2].value_int,
            ]
            inc_list = list(
                range(lookup_list[0], lookup_list[0] + len(lookup_list))
            )

            if lookup_list == inc_list:
                return True
            curr_ptr += 1

        return False

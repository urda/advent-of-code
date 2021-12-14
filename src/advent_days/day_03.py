"""
Copyright 2021 Peter Urda

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

from enum import Enum
from typing import (
    List,
    Tuple,
)

from .day_meta import DayMeta


class LifeSupportFilterMode(Enum):
    """
    Enum to flip between filter modes
    """
    CO2 = 'CO2'
    O2 = 'O2'


class Day03(DayMeta):
    """
    Advent Day 03
    """

    _data_file = 'day_03.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_gamma, part_1_epsilon = cls.perform_part_1(
            cls.get_lines_as_list_of_integer_lists(cls._data_file)
        )
        part_2_o2, part_2_co2 = cls.perform_part_2(
            cls.get_lines_as_list_of_integer_lists(cls._data_file)
        )

        return [
            'Part 1:',
            f'Determined Gamma: {part_1_gamma}',
            f'Determined Epsilon: {part_1_epsilon}',
            f'Determined: {part_1_gamma * part_1_epsilon}',
            '---',
            'Part 2',
            f'Determined O2: {part_2_o2}',
            f'Determined CO2: {part_2_co2}',
            f'Determined: {part_2_o2 * part_2_co2}',
        ]

    @classmethod
    def perform_part_1(
            cls,
            binary_values: List[List[int]]
    ) -> Tuple[int, int]:
        """
        Compute the answer to part 1 for Day 03.

        :param binary_values: The values to process for the day.
        :return: The results as a tuple: (Gamma Rate, Epsilon Rate)
        """

        # Configure result storage list
        parse_results = None

        # Given each entry from input, examine each bit position and record
        for binary_data in binary_values:
            if not parse_results:
                parse_results = [0] * len(binary_data)

            for idx, bit_value in enumerate(binary_data):
                if bit_value == 1:
                    parse_results[idx] += 1

        result_count = len(binary_values) // 2
        gamma_rate_values = []
        epsilon_rate_values = []

        # For each bit position in the results, determine truthiness
        for bit_count in parse_results:
            gamma_rate_truth = bit_count >= result_count
            gamma_rate_values.append(int(gamma_rate_truth))
            epsilon_rate_values.append(int(not gamma_rate_truth))

        gamma_rate_values = \
            int(''.join(str(bit) for bit in gamma_rate_values), 2)
        epsilon_rate_values = \
            int(''.join(str(bit) for bit in epsilon_rate_values), 2)

        return gamma_rate_values, epsilon_rate_values

    @classmethod
    def _compute_life_support_value(
            cls,
            binary_values: List[List[int]],
            life_support: LifeSupportFilterMode
    ) -> List[int]:
        result = None
        binary_length = len(binary_values[0])

        for idx in range(binary_length):
            seen_zeros = 0
            seen_ones = 0
            for binary_data in binary_values:
                if binary_data[idx] == 0:
                    seen_zeros += 1
                elif binary_data[idx] == 1:
                    seen_ones += 1

            rebuild_list = []
            for binary_data in binary_values:
                match life_support:
                    case LifeSupportFilterMode.CO2:
                        if seen_ones < seen_zeros:
                            if binary_data[idx] == 1:
                                rebuild_list.append(binary_data)
                        else:
                            if binary_data[idx] == 0:
                                rebuild_list.append(binary_data)
                    case LifeSupportFilterMode.O2:
                        if seen_ones >= seen_zeros:
                            if binary_data[idx] == 1:
                                rebuild_list.append(binary_data)
                        else:
                            if binary_data[idx] == 0:
                                rebuild_list.append(binary_data)
            binary_values = rebuild_list

            if len(binary_values) == 1:
                result = binary_values.pop(0)
                break

        if result is None:
            raise ValueError(f'Something went wrong when parsing the input '
                             f'for {life_support}')

        return result

    @classmethod
    def perform_part_2(cls, binary_values: List[List[int]]) -> Tuple[int, int]:
        """
        Compute the answer to part 2 for Day 03.

        :param binary_values: The values to process for the day.
        :return: The results as a tuple: (O2 Result, CO2 Result)
        """
        o2_gen_value = \
            cls._compute_life_support_value(binary_values,
                                            LifeSupportFilterMode.O2)
        co2_gen_value = \
            cls._compute_life_support_value(binary_values,
                                            LifeSupportFilterMode.CO2)

        o2_result = \
            int(''.join(str(bit) for bit in o2_gen_value), 2)
        co2_result = \
            int(''.join(str(bit) for bit in co2_gen_value), 2)

        return o2_result, co2_result

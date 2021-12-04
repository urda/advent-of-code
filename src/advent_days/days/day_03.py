from enum import Enum
from typing import List

from .day_meta import DayMeta


class LifeSupportFilterMode(Enum):
    CO2 = 'CO2'
    O2 = 'O2'


class Day03(DayMeta):
    _binary_value_length = 12
    _data_file = 'day_03_data.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_gamma, part_1_epsilon = cls._perform_part_1()
        part_2_o2, part_2_co2 = cls._perform_part_2()

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
    def _get_lines(cls) -> List[List[int]]:
        lines = []
        with open(cls.data_dir_path(cls._data_file), 'r') as data_file:
            for line in data_file:
                # Strip new line element, convert to ints
                lines.append([int(i) for i in list(line)[:-1]])
        return lines

    @classmethod
    def _perform_part_1(cls) -> (int, int):
        binary_values = cls._get_lines()

        # Configure result storage list
        parse_results = [0] * cls._binary_value_length

        # Given each entry from input, examine each bit position and record
        for binary_data in binary_values:
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
            life_support: LifeSupportFilterMode
    ) -> List[int]:
        result = None
        binary_values = cls._get_lines()

        for idx in range(cls._binary_value_length):
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
    def _perform_part_2(cls) -> (int, int):
        o2_gen_value = \
            cls._compute_life_support_value(LifeSupportFilterMode.O2)
        co2_gen_value = \
            cls._compute_life_support_value(LifeSupportFilterMode.CO2)

        o2_result = \
            int(''.join(str(bit) for bit in o2_gen_value), 2)
        co2_result = \
            int(''.join(str(bit) for bit in co2_gen_value), 2)

        return o2_result, co2_result

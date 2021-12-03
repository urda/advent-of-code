from pathlib import Path
from typing import List


class Day03:
    _working_dir = Path(__file__).resolve().parent

    _data_file = 'day_03_data.txt'
    _data_file_path = Path(_working_dir, _data_file)

    _binary_value_length = 12

    @classmethod
    def diagnose_sub(cls):
        part_1_gamma, part_1_epsilon = cls._perform_part_1()

        print('Part 1:')
        print(f'Determined Gamma: {part_1_gamma}')
        print(f'Determined Epsilon: {part_1_epsilon}')
        print(f'Determined: {part_1_gamma * part_1_epsilon}')

    @classmethod
    def _get_lines(cls) -> List[List[int]]:
        lines = []
        with open(cls._data_file_path, 'r') as data_file:
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

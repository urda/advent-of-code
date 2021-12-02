from pathlib import Path
from typing import List


class Day02:
    _working_dir = Path(__file__).resolve().parent

    _data_file = 'day_02_data.txt'
    _data_file_path = Path(_working_dir, _data_file)

    @classmethod
    def drive_sub(cls):
        part_1_horizontal_pos, part_1_depth_pos = cls._perform_part_1()
        part_2_horizontal_pos, part_2_depth_pos = cls._perform_part_2()

        print('Part 1:')
        print(f'Determined Horizontal: {part_1_horizontal_pos}')
        print(f'Determined Depth: {part_1_depth_pos}')
        print(f'Determined: {part_1_horizontal_pos * part_1_depth_pos}')
        print('---')
        print('Part 2')
        print(f'Determined Horizontal: {part_2_horizontal_pos}')
        print(f'Determined Depth: {part_2_depth_pos}')
        print(f'Determined: {part_2_horizontal_pos * part_2_depth_pos}')

    @classmethod
    def _get_lines(cls) -> List[str]:
        lines = []
        with open(cls._data_file_path, 'r') as data_file:
            for line in data_file:
                lines.append(line)
        return lines

    @classmethod
    def _perform_part_1(cls) -> (int, int):
        commands = cls._get_lines()

        horizontal_pos = 0
        depth_pos = 0

        for command in commands:
            raw_direction, raw_distance = command.split(' ')
            direction = raw_direction.lower()
            distance = int(raw_distance)

            match direction:
                case 'down':
                    depth_pos += distance
                case 'forward':
                    horizontal_pos += distance
                case 'up':
                    depth_pos -= distance
                case _:
                    raise ValueError(f'Cannot process command "{direction}"')

        return horizontal_pos, depth_pos

    @classmethod
    def _perform_part_2(cls):
        commands = cls._get_lines()

        horizontal_pos = 0
        depth_pos = 0
        aim_value = 0

        for command in commands:
            raw_direction, raw_distance = command.split(' ')
            direction = raw_direction.lower()
            distance = int(raw_distance)

            match direction:
                case 'down':
                    aim_value += distance
                case 'forward':
                    horizontal_pos += distance
                    depth_pos += aim_value * distance
                case 'up':
                    aim_value -= distance
                case _:
                    raise ValueError(f'Cannot process command "{direction}"')

        return horizontal_pos, depth_pos

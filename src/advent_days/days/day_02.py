from typing import List

from .day_meta import DayMeta


class Day02(DayMeta):
    _data_file = 'day_02_data.txt'

    @classmethod
    def solve_day(cls) -> List[str]:
        part_1_horizontal_pos, part_1_depth_pos = cls._perform_part_1()
        part_2_horizontal_pos, part_2_depth_pos = cls._perform_part_2()

        return [
            'Part 1:',
            f'Determined Horizontal: {part_1_horizontal_pos}',
            f'Determined Depth: {part_1_depth_pos}',
            f'Determined: {part_1_horizontal_pos * part_1_depth_pos}',
            '---',
            'Part 2',
            f'Determined Horizontal: {part_2_horizontal_pos}',
            f'Determined Depth: {part_2_depth_pos}',
            f'Determined: {part_2_horizontal_pos * part_2_depth_pos}',
        ]

    @classmethod
    def _get_lines(cls) -> List[str]:
        lines = []
        with open(cls.data_dir_path(cls._data_file), 'r') as data_file:
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

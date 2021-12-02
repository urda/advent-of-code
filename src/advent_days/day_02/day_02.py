from pathlib import Path
from typing import List


class Day02:
    _working_dir = Path(__file__).resolve().parent

    _data_file = 'day_02_data.txt'
    _data_file_path = Path(_working_dir, _data_file)

    _understood_commands = [
        'down',
        'forward',
        'up',
    ]

    @classmethod
    def drive_sub(cls):
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

        print(f'Determined Horizontal: {horizontal_pos}')
        print(f'Determined Depth: {depth_pos}')
        print(f'Determined: {horizontal_pos * depth_pos}')

    @classmethod
    def _get_lines(cls) -> List[str]:
        lines = []
        with open(cls._data_file_path, 'r') as data_file:
            for line in data_file:
                lines.append(line)
        return lines

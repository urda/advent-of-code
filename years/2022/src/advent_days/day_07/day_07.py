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

from typing import List

from .elf_dir import ElfDir
from .elf_file import ElfFile
from ..day_meta import DayMeta


class Day07(DayMeta):
    """
    Advent of Code 2022, Day 07
    """

    _cmd_dir = '$ cd '
    _cmd_list = '$ ls'
    _cmd_parent = '$ cd ..'
    _cmd_root = '$ cd /'

    _fs_max_size = 70000000
    _fs_free_space = 30000000

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_07.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param data: The raw data from Advent of Code
        :returns: The result for Part 1
        """

        root_dir = cls._parse_data(data)

        search_space = [root_dir]
        running_total = 0

        while len(search_space) > 0:
            curr_dir = search_space.pop()

            curr_dir_size = curr_dir.size
            if curr_dir_size <= 100000:
                running_total += curr_dir_size

            for child_dir in curr_dir.directories:
                search_space.append(child_dir)

        return running_total

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and convert into an understood format and compute.

        :param data: The raw data from Advent of Code
        :returns: The result for Part 2
        """

        root_dir = cls._parse_data(data)

        search_space = [root_dir]
        used_size = root_dir.size
        free_size = cls._fs_max_size - used_size
        target_free = cls._fs_free_space - free_size

        if target_free < 0:
            return 0

        best_result = cls._fs_max_size
        while len(search_space) > 0:
            curr_dir = search_space.pop()

            curr_dir_size = curr_dir.size
            if target_free <= curr_dir_size < best_result:
                best_result = curr_dir_size

            for child_dir in curr_dir.directories:
                search_space.append(child_dir)

        return best_result

    @classmethod
    def _parse_data(cls, data: List[str]) -> ElfDir:
        if data[0] != cls._cmd_root:
            raise NotImplementedError('Invalid file')

        root = ElfDir('/')
        pointer = root

        for raw_data in data[1:]:
            if raw_data == cls._cmd_root:
                pointer = root

            elif raw_data == cls._cmd_parent:
                pointer = pointer.parent

            elif raw_data[0].isdigit():
                file_size, file_name = raw_data.split(' ')
                pointer.add_thing(ElfFile(file_name, int(file_size)))

            elif raw_data.startswith(cls._cmd_dir):
                dir_name = raw_data.split(cls._cmd_dir)[1]
                new_node = ElfDir(dir_name, pointer)
                pointer.add_thing(new_node)
                pointer = new_node

        return root

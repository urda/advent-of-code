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

import os

from advent_utils.copyright_builder import CopyrightBuilder


class HenryPlateRefs:
    """
    Henry Plate Builder - Source Code Needs
    """

    @classmethod
    def get_src_file_contents(
            cls,
            year_token: int,
            day_token: int,
    ) -> str:
        """
        Get the main source file contents

        :param day_token: The advent day number to use.
        :return: The henry plate source code.
        """

        file_contents = [
            CopyrightBuilder.get_copyright_current_year_only(),
            '',
            'from typing import List',
            '',
            'from ..day_meta import DayMeta',
            '',
            '',
            f'class Day{day_token:02d}(DayMeta):',
            '    """',
            f'    Advent of Code {year_token}, '
            f'Day {day_token:02d}',
            '    """',
            '',
            '    @classmethod',
            '    def solve_day(cls) -> List[str]:',
            '        raw_data = cls.get_lines_as_list_string('
            f'\'day_{day_token:02d}.txt\')',
            '',
            '        return [',
            '            str(cls.compute_part_1(raw_data)),',
            '            str(cls.compute_part_2(raw_data)),',
            '        ]',
            '',
            '    @classmethod',
            '    def compute_part_1(cls, data: List[str]) -> int:',
            '        """',
            f'        Parse the data and compute for Day {day_token:02d}.',
            '        :param data: The data from Advent of Code.',
            '        :returns: The result for Part 1.',
            '        """',
            '        return -1',
            '',
            '    @classmethod',
            '    def compute_part_2(cls, data: List[str]) -> int:',
            '        """',
            f'        Parse the data and compute for Day {day_token:02d}.',
            '        :param data: The data from Advent of Code.',
            '        :returns: The result for Part 2.',
            '        """',
            '        return -1',
            '',
        ]

        return os.linesep.join(file_contents)

    @classmethod
    def get_init_file_contents(cls, day_token: int) -> str:
        """
        Get the __init__ file contents

        :param day_token: The advent day number to use.
        :return: The henry plate __init__ code.
        """

        file_contents = [
            CopyrightBuilder.get_copyright_current_year_only(),
            '',
            f'from .day_{day_token:02d} import Day{day_token:02d}',
            '',
            '',
            '__all__ = [',
            f'    \'Day{day_token:02d}\',',
            ']',
            '',
        ]

        return os.linesep.join(file_contents)

    @classmethod
    def get_test_file_contents(
            cls,
            year_token: int,
            day_token: int,
    ) -> str:
        """
        Get the test file contents

        :param year_token: The advent year number to use.
        :param day_token: The advent day number to use.
        :return: The henry plate test code.
        """
        file_contents = [
            CopyrightBuilder.get_copyright_current_year_only(),
            '',
            'from unittest import TestCase',
            '',
            f'from advent_years.y{year_token} import Day{day_token:02d}',
            '',
            '',
            f'class TestDay{day_token:02d}(TestCase):',
            '    data = [',
            '    ]',
            '',
            cls._build_test_block(day_token, 1),
            '',
            cls._build_test_block(day_token, 2),
            '',
        ]

        return os.linesep.join(file_contents)

    @classmethod
    def _build_test_block(cls, day_token: int, part_num: int) -> str:
        data = [
            f'    def test_part_{part_num}(self):',
            '        expected = 1234',
            f'        actual = Day{day_token}'
            f'.compute_part_{part_num}(self.data)',
            '        assert expected == actual',
        ]

        return os.linesep.join(data)

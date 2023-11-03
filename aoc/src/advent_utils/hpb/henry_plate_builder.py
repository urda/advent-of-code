"""
Copyright 2022-2023 Peter Urda

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

import datetime
import os
from pathlib import Path
from typing import (
    List,
    Tuple,
)

from advent_utils.copyright_builder import CopyrightBuilder
from advent_utils.hpb.henry_plate_refs import HenryPlateRefs


class HenryPlateBuilder:
    """
    Automate your Advent Days with Henry Plates

    Dedicated to Henry Poon
    """

    @classmethod
    def build_src_root_path(cls) -> Path:
        """
        Get the source code root folder

        :return: A 'Path' object for the file path.
        """
        meta_dir = cls._internal_master_root()
        return Path(meta_dir, 'src/')

    @classmethod
    def build_tests_root_path(cls) -> Path:
        """
        Get the tests code root folder

        :return: A 'Path' object for the file path.
        """
        meta_dir = cls._internal_master_root()
        return Path(meta_dir, 'tests/')

    @classmethod
    def create_files_with_content(cls, files: List[Tuple[Path, str]]) -> None:
        """
        Given a collection of "files", create them with given content.

        :param files: A list of tuples where (Path, content)
        """
        for file_path, file_content in files:
            with open(file_path, 'w+', encoding='utf-8') as new_file:
                print(f'Creating "{file_path.as_posix()}" ...')
                new_file.write(file_content)

    @classmethod
    def modify_advent_init(cls, file_path: Path, day_token: int) -> None:
        """
        Modify the '__init__' file to introduce new days for imports.

        :param file_path: The Path object to Advent Days root __init__
        :param day_token: The advent day number.
        """
        with open(file_path, 'r', encoding='utf-8') as init_file:
            contents = init_file.readlines()

        # As lines are inserted, later indexes have to reflect that
        copy_idx_mark = 1
        import_idx_mark = contents.index('__all__ = [' + os.linesep) - 1
        class_idx_mark = len(contents)

        day_id = f'{day_token:02d}'
        years = f'2021-{datetime.date.today().year}'
        contents[copy_idx_mark] = \
            f'{CopyrightBuilder.get_years_line_only(years)}{os.linesep}'
        contents.insert(
            import_idx_mark,
            f'from .day_{day_token:02d} import Day{day_id}{os.linesep}'
        )
        contents.insert(class_idx_mark, f'    \'Day{day_id}\',{os.linesep}')

        with open(file_path, 'w', encoding='utf-8') as init_file:
            print(f'Updating "{file_path.as_posix()}" ...')
            init_file.writelines(contents)

    @classmethod
    def modify_main_copyright(cls, file_path: Path) -> None:
        """
        Modify the 'main.py' program's copyright.

        :param file_path: The Path object to 'main.py'.
        """

        with open(file_path, 'r', encoding='utf-8') as main_py:
            contents = main_py.readlines()

        # We seek nearby anchors, thinking about file shifts as we go
        copy_idx_mark = 2
        years = f'2021-{datetime.date.today().year}'
        contents[copy_idx_mark] = \
            f'{CopyrightBuilder.get_years_line_only(years)}{os.linesep}'

        with open(file_path, 'w', encoding='utf-8') as main_py:
            print(f'Updating "{file_path.as_posix()}" ...')
            main_py.writelines(contents)

    @classmethod
    def pre_stage_day(cls) -> None:
        """
        Perform all the required interactions and work to pre-stage a day.
        """
        # pylint: disable=too-many-locals

        print()
        print('[HPB]')
        print()

        year_input = input('Enter an advent year number: ')
        year_parsed = int(year_input) if year_input.isdigit() else None
        day_input = input('Enter an advent day number: ')
        day_parsed = int(day_input) if day_input.isdigit() else None

        match day_parsed:
            case [None, 0]:
                print('Invalid selection')
                return
            case _:
                day_token = day_parsed

        print(f'~~~ Will use value \'{day_token}\' ~~~')
        print()

        print('This operation is ** D E S T R U C T I V E ** are you sure ?')
        confirm_change = input('Enter "Y" to continue, anything else quits: ')
        confirm_parsed = confirm_change if confirm_change.isascii() else None
        if confirm_parsed != 'Y':
            print('No changes made.')
            return

        print()
        print('OK I warned you.')
        print()

        # This content is always created each day
        init_day_file_str = HenryPlateRefs.get_init_file_contents(day_token)
        src_day_file_str = HenryPlateRefs.get_src_file_contents(day_token)
        test_day_file_str = HenryPlateRefs.get_test_file_contents(
            year_parsed,
            day_token
        )

        init_file_path = Path(
            cls.build_src_root_path(),
            f'advent_years/y{year_parsed}/day_{day_token:02d}/__init__.py'
        )
        src_file_path = Path(
            cls.build_src_root_path(),
            f'advent_years/y{year_parsed}/'
            f'day_{day_token:02d}/day_{day_token:02d}.py'
        )
        test_file_path = Path(
            cls.build_tests_root_path(),
            f'advent_years/y{year_parsed}/test_day_{day_token:02d}.py'
        )

        print(f'Creating directory "{init_file_path.parent.as_posix()}" ...')
        os.makedirs(init_file_path.parent, exist_ok=True)
        new_pairings = [
            (init_file_path, init_day_file_str),
            (src_file_path, src_day_file_str),
            (test_file_path, test_day_file_str),
        ]
        cls.create_files_with_content(new_pairings)

        # These files need to be "updated" when a new day is added.
        advent_init_path = Path(cls.build_src_root_path(),
                                f'advent_years/y{year_parsed}/__init__.py')
        main_file_path = Path(cls.build_src_root_path(),
                              'main.py')

        # Perform modifications
        cls.modify_advent_init(advent_init_path, day_token)
        cls.modify_main_copyright(main_file_path)

    @classmethod
    def _internal_master_root(cls) -> Path:
        """
        (Internal) Get real root ref.
        """
        return Path(__file__).resolve().parent.parent.parent.parent

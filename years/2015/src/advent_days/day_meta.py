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

from abc import (
    ABC,
    abstractmethod,
)
from pathlib import Path
from typing import List


class DayMeta(ABC):
    """
    Meta "abstract base class" for the Advent Day challenges.
    """

    @classmethod
    def build_data_file_path(cls, data_file_name: str) -> Path:
        """
        Allow advent days to build a path to a data file stored in
        the project data file folder.

        :param data_file_name: The data file to build a path to.
        :return: A 'Path' object for the file path.
        """
        meta_dir = Path(__file__).resolve().parent.parent.parent
        return Path(meta_dir, f'data/{data_file_name}')

    @classmethod
    def get_csv_line_as_integer_list(cls, data_file_name: str) -> List[int]:
        """
        Given a data file name, read out the first line from it as a string
        of CSV entries of integers.

        :param data_file_name: The data file to lookup in the project.
        :return: A Python list of integers from the line of CSV values.
        """
        data_path = cls.build_data_file_path(data_file_name)
        with open(data_path, 'r', encoding='utf-8') as data_file:
            raw_data_line = data_file.readline().strip()

        return [int(x) for x in raw_data_line.split(',')]

    @classmethod
    def get_lines_as_list_string(cls, data_file_name: str) -> List[str]:
        """
        Given a data file name, read out the lines from it into a Python
        list of strings.

        :param data_file_name: The data file to lookup in the project.
        :return: A Python list of strings of each line.
        """
        data_path = cls.build_data_file_path(data_file_name)

        lines = []
        with open(data_path, 'r', encoding='utf-8') as data_file:
            for line in data_file:
                lines.append(line.strip())
        return lines

    @classmethod
    def get_lines_as_list_string_rstrip(cls, data_file_name: str) -> List[str]:
        """
        Given a data file name, read out the lines from it into a Python
        list of strings, with ".rstrip()" applied to each line.

        :param data_file_name: The data file to lookup in the project.
        :return: A Python list of strings of each line.
        """
        data_path = cls.build_data_file_path(data_file_name)

        lines = []
        with open(data_path, 'r', encoding='utf-8') as data_file:
            for line in data_file:
                lines.append(line.rstrip())
        return lines

    @classmethod
    def get_lines_as_list_of_integer_lists(
            cls,
            data_file_name: str
    ) -> List[List[int]]:
        """
        Given a data file name, read out the lines from it into a python list
        of lists of integers.

        :param data_file_name: The data file to lookup in the project.
        :return: A Python list of lists of integers of each line.
        """
        data_path = cls.build_data_file_path(data_file_name)
        lines = []
        with open(data_path, 'r', encoding='utf-8') as data_file:
            for line in data_file:
                # Strip new line element, convert to ints
                lines.append([int(i) for i in list(line.strip())])
        return lines

    @classmethod
    @abstractmethod
    def solve_day(cls) -> List[str]:
        """
        Method that advent days should use for solving.
        :return: A list of string values for the program output.
        """

    @classmethod
    def solve_day_and_print(cls) -> None:
        """
        Solve the actual day, and print each output line.
        :return: None
        """
        for output_line in cls.solve_day():
            print(output_line)

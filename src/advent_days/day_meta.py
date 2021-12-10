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

from abc import (
    ABC,
    abstractmethod,
)
from pathlib import Path
from typing import List


class DayMeta(ABC):
    @classmethod
    def build_data_file_path(cls, data_file_name: str) -> Path:
        meta_dir = Path(__file__).resolve().parent.parent.parent
        return Path(meta_dir, f'data/{data_file_name}')

    @classmethod
    @abstractmethod
    def solve_day(cls) -> List[str]:
        pass

    @classmethod
    def solve_day_and_print(cls):
        for output_line in cls.solve_day():
            print(output_line)

"""
Copyright 2023 Peter Urda

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

from typing import (
    Dict,
    List,
    Tuple,
)

from .sue_data import SueData
from ..day_meta import DayMeta


class Day16(DayMeta):
    """
    Advent of Code 2015, Day 16
    """

    _target_sue = SueData(
        sue_id=0,
        children=3,
        cats=7,
        samoyeds=2,
        pomeranians=3,
        akitas=0,
        vizslas=0,
        goldfish=5,
        trees=3,
        cars=2,
        perfumes=1,
    )

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_16.txt')

        return [
            str(cls.compute_part_1(raw_data, cls._target_sue)),
            str(cls.compute_part_2(raw_data, cls._target_sue)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str], target_sue: SueData) -> int:
        """
        Parse the data and compute for Day 16.
        :param data: The data from Advent of Code.
        :param target_sue: The target Sue to find.
        :returns: The result for Part 1.
        """
        sues = cls._parse_sues(data)
        result_sue = cls._find_sue(sues, target_sue)
        return result_sue.sue_id

    @classmethod
    def compute_part_2(cls, data: List[str], target_sue: SueData) -> int:
        """
        Parse the data and compute for Day 16.
        :param data: The data from Advent of Code.
        :param target_sue: The target Sue to find.
        :returns: The result for Part 2.
        """
        sues = cls._parse_sues(data)
        result_sue = cls._find_turbo(sues, target_sue)
        return result_sue.sue_id

    @classmethod
    def _find_sue(cls, sues: List[SueData], target_sue: SueData) -> SueData:
        """
        Locate the Sue in the haystack.
        """
        for possible_sue in sues:
            if cls._sue_conflict_exists(possible_sue, target_sue):
                continue
            return possible_sue
        raise ValueError('No Sue Found')

    @classmethod
    def _find_turbo(cls, sues: List[SueData], target_sue: SueData) -> SueData:
        """
        Locate the Sue in the haystack, accounting for the retroencabulator.
        """
        for possible_sue in sues:
            if cls._sue_conflict_exists_turbo(possible_sue, target_sue):
                continue
            return possible_sue
        raise ValueError('No sue Found')

    @classmethod
    def _parse_sues(cls, sue_data: List[str]) -> List[SueData]:
        """
        Given raw sue data, create a list of Sues
        """
        sues = []
        for raw_sue in sue_data:
            sue_id, sue_values = raw_sue.split(':', 1)
            sue_id = int(sue_id.strip().split(' ')[1])
            sue_values = sue_values.strip().split(', ')

            sue_value_map = cls._parse_sue_datapoints(sue_values)
            sue_data = SueData(sue_id, **sue_value_map)
            sues.append(sue_data)
        return sues

    @classmethod
    def _parse_sue_datapoint(cls, sue_value: str) -> Tuple[str, int]:
        """
        Parse a sue datapoint token.
        """
        raw_key, raw_value = sue_value.split(': ')
        return raw_key, int(raw_value)

    @classmethod
    def _parse_sue_datapoints(cls, sue_values: List[str]) -> Dict[str, int]:
        """
        Given the raw sue data points, create a dictionary of values from it.
        """
        sue_datapoints = {}
        for sue_value in sue_values:
            key, value = cls._parse_sue_datapoint(sue_value)
            sue_datapoints[key] = value
        return sue_datapoints

    @classmethod
    def _sue_conflict_exists(cls, sue: SueData, target_sue: SueData) -> bool:
        """
        Report if the given sue conflicts with the target sue.
        """
        sue_values = sue.set_values_as_dict()
        target_values = target_sue.values_as_dict()
        for sue_key, sue_value in sue_values.items():
            if target_values[sue_key] != sue_value:
                return True
        return False

    @classmethod
    def _sue_conflict_exists_turbo(
            cls,
            sue: SueData,
            target_sue: SueData
    ) -> bool:
        """
        Report if the given sue conflicts with the target sue,
        retroencabulator variant.
        """
        upscale_check = ('cats', 'trees')
        downscale_check = ('goldfish', 'pomeranians')
        sue_values = sue.set_values_as_dict()
        target_sue_values = target_sue.values_as_dict()
        for key, value in sue_values.items():
            if key in upscale_check:
                if value <= target_sue_values[key]:
                    return True
            elif key in downscale_check:
                if value >= target_sue_values[key]:
                    return True
            else:
                if value != target_sue_values[key]:
                    return True
        return False

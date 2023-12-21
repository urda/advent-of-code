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

from typing import List
from unittest import TestCase

from advent_years.y2023 import Day16


class TestDay16(TestCase):
    data = [
        r'.|...\.... ',
        r'|.-.\..... ',
        r'.....|-... ',
        r'........|. ',
        r'.......... ',
        r'.........\ ',
        r'..../.\\.. ',
        r'.-.-/..|.. ',
        r'.|....-|.\ ',
        r'..//.|.... ',
    ]

    def test_part_1(self):
        expected = 46
        actual = Day16.compute_part_1(self._clean_data(self.data))
        assert expected == actual

    def test_part_2(self):
        expected = 51
        actual = Day16.compute_part_2(self._clean_data(self.data))
        assert expected == actual

    @staticmethod
    def _clean_data(data: List[str]) -> List[str]:
        new_data = []
        for line in data:
            new_data.append(line.rstrip())
        return new_data

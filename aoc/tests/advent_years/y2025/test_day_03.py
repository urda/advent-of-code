"""
Copyright 2025 Peter Urda

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

from unittest import TestCase

from advent_years.y2025 import Day03


class TestDay03(TestCase):
    data = [
        '987654321111111',
        '811111111111119',
        '234234234234278',
        '818181911112111',
    ]

    def test_part_1(self):
        expected = 357
        actual = Day03.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 3121910778619
        actual = Day03.compute_part_2(self.data)
        assert expected == actual

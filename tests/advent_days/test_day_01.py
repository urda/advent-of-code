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

from unittest import TestCase

from advent_days import Day01


class TestDay01(TestCase):
    data = [
        '1000',
        '2000',
        '3000',
        '',
        '4000',
        '',
        '5000',
        '6000',
        '',
        '7000',
        '8000',
        '9000',
        '',
        '10000',
        '',
    ]

    def test_part_1(self):
        expected = 24000
        actual = Day01.compute_part_1(Day01.parse_data(self.data))
        assert expected == actual

    def test_part_2(self):
        expected = 45000
        actual = Day01.compute_part_2(Day01.parse_data(self.data))
        assert expected == actual

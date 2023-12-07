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

from unittest import TestCase

from advent_years.y2023 import Day01


class TestDay01(TestCase):
    def test_part_1(self):
        test_data = [
            '1abc2',
            'pqr3stu8vwx',
            'a1b2c3d4e5f',
            'treb7uchet',
        ]

        expected = 142
        actual = Day01.compute_part_1(test_data)
        assert expected == actual

    def test_part_2(self):
        test_data = [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
        ]
        expected = 281
        actual = Day01.compute_part_2(test_data)
        assert expected == actual

        expected = 22
        actual = Day01.compute_part_2(['25xmvshkbmtkmvqpfhgq8fivefqctjm6two'])
        assert expected == actual

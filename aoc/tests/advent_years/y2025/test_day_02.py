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

from advent_years.y2025 import Day02


class TestDay02(TestCase):
    data = [
        '11-22',
        '95-115',
        '998-1012',
        '1188511880-1188511890',
        '222220-222224',
        '1698522-1698528',
        '446443-446449',
        '38593856-38593862',
        '565653-565659',
        '824824821-824824827',
        '2121212118-2121212124',
    ]

    def test_part_1(self):
        expected = 1227775554
        actual = Day02.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 4174379265
        actual = Day02.compute_part_2(self.data)
        assert expected == actual

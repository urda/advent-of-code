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

from advent_years.y2015 import Day03


class TestDay03(TestCase):
    def test_part_1(self):
        data = [
            ('>', 2),
            ('^>v<', 4),
            ('^v^v^v^v^v', 2),
        ]

        for test_entry in data:
            test_entry_data, expected = test_entry
            actual = Day03.compute_part_1(test_entry_data)
            assert expected == actual

    def test_part_2(self):
        data = [
            ('^v', 3),
            ('^>v<', 3),
            ('^v^v^v^v^v', 11),
        ]

        for test_entry in data:
            test_entry_data, expected = test_entry
            actual = Day03.compute_part_2(test_entry_data)
            assert expected == actual

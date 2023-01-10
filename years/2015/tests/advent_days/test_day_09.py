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

from advent_days import Day09


class TestDay09(TestCase):
    data = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141',
    ]

    def test_part_1(self):
        expected = 605
        actual = Day09.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 982
        actual = Day09.compute_part_2(self.data)
        assert expected == actual

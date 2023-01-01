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

from advent_days import Day14


class TestDay14(TestCase):
    data = [
        '498,4 -> 498,6 -> 496,6',
        '503,4 -> 502,4 -> 502,9 -> 494,9',
    ]

    def test_part_1(self):
        expected = 24
        actual = Day14.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 93
        actual = Day14.compute_part_2(self.data)
        assert expected == actual

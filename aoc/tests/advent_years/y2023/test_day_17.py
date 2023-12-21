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

from advent_years.y2023 import Day17


class TestDay17(TestCase):
    data = [
        [2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3],
        [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3],
        [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4],
        [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2],
        [4, 5, 4, 6, 6, 5, 7, 8, 6, 7, 5, 3, 6],
        [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4],
        [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6],
        [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3],
        [4, 6, 5, 4, 9, 6, 7, 9, 8, 6, 8, 8, 7],
        [4, 5, 6, 4, 6, 7, 9, 9, 8, 6, 4, 5, 3],
        [1, 2, 2, 4, 6, 8, 6, 8, 6, 5, 5, 6, 3],
        [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 3, 5],
        [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 5, 3, 3],
    ]

    def test_part_1(self):
        expected = 102
        actual = Day17.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 94
        actual = Day17.compute_part_2(self.data)
        assert expected == actual

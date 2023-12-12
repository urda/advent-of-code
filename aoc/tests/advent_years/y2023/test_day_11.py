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

from advent_years.y2023 import Day11


class TestDay11(TestCase):
    data = [
        '...#......',
        '.......#..',
        '#.........',
        '..........',
        '......#...',
        '.#........',
        '.........#',
        '..........',
        '.......#..',
        '#...#.....',
    ]

    def test_part_1(self):
        expected = 374
        actual = Day11.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        tests = [
            (self.data, 10, 1030),
            (self.data, 100, 8410),
        ]

        for data, factor, expected in tests:
            actual = Day11._shortest_paths(data, factor)
            assert expected == actual

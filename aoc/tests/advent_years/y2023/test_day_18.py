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

from advent_years.y2023 import Day18


class TestDay18(TestCase):
    data = [
        'R 6 (#70c710)',
        'D 5 (#0dc571)',
        'L 2 (#5713f0)',
        'D 2 (#d2c081)',
        'R 2 (#59c680)',
        'D 2 (#411b91)',
        'L 5 (#8ceee2)',
        'U 2 (#caa173)',
        'L 1 (#1b58a2)',
        'U 2 (#caa171)',
        'R 2 (#7807d2)',
        'U 3 (#a77fa3)',
        'L 2 (#015232)',
        'U 2 (#7a21e3)',
    ]

    def test_part_1(self):
        expected = 62
        actual = Day18.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 952408144115
        actual = Day18.compute_part_2(self.data)
        assert expected == actual

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

from advent_years.y2015 import Day18


class TestDay18(TestCase):
    data = [
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..',
    ]

    def test_part_1(self):
        expected = 4
        actual = Day18.run_grid(self.data, 4, False)
        assert expected == actual

    def test_part_2(self):
        expected = 17
        actual = Day18.run_grid(self.data, 5, True)
        assert expected == actual

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

from advent_years.y2022 import Day19


class TestDay19(TestCase):
    data = [
        'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 '
        'ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot '
        'costs 2 ore and 7 obsidian.',
        'Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 '
        'ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot '
        'costs 3 ore and 12 obsidian.',
    ]

    def test_part_1(self):
        expected = 33
        actual = Day19.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 3472
        actual = Day19.compute_part_2(self.data)
        assert expected == actual

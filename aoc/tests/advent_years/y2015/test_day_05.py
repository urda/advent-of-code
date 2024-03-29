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

from advent_years.y2015 import Day05


class TestDay05(TestCase):
    def test_part_1(self):
        # noinspection SpellCheckingInspection
        data = [
            'ugknbfddgicrmopn',
            'aaa',
            'jchzalrnumimnmhp',
            'haegwjzuvuyypxyu',
            'dvszwmarrgswjxmb',
        ]
        expected = 2
        actual = Day05.compute_part_1(data)
        assert expected == actual

    def test_part_2(self):
        # noinspection SpellCheckingInspection
        data = [
            'qjhvhtzxzqqjkmpb',
            'xxyxx',
            'uurcxstgmygtbstg',
            'ieodomkazucvgmuy',
        ]
        expected = 2
        actual = Day05.compute_part_2(data)
        assert expected == actual

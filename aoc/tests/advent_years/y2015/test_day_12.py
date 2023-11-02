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

from advent_years.y2015 import Day12


class TestDay12(TestCase):
    def test_part_1(self):
        expected = 3
        actual = Day12.compute_part_1('{"a":{"b":4},"c":-1}')
        assert expected == actual

    def test_part_2(self):
        expected = 4
        actual = Day12.compute_part_2('[1,{"c":"red","b":2},3]')
        assert expected == actual

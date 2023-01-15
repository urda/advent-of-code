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

from advent_days import Day10


class TestDay10(TestCase):
    data = [
        (1, 82350),
        (11, 107312),
        (21, 139984),
        (1211, 182376),
        (111221, 237746),
    ]

    def test_iterations(self):
        for test_input, expected in self.data:
            actual_input = list(map(int, str(test_input)))
            actual = Day10.compute_part_1(actual_input)
            assert expected == actual

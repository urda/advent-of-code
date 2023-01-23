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

from advent_days import Day14


class TestDay14(TestCase):
    data = [
        'Comet can fly 14 km/s for 10 seconds, '
        'but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, '
        'but then must rest for 162 seconds.',
    ]

    time = 1000

    def test_part_1_and_2(self):
        parts = Day14.compute_parts(self.data, self.time)

        pt1_expected = 1120
        pt1_actual = Day14.compute_part_1(parts)
        assert pt1_expected == pt1_actual

        pt2_expected = 689
        pt2_actual = Day14.compute_part_2(parts)
        assert pt2_expected == pt2_actual

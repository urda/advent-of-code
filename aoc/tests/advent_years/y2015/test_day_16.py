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

from advent_years.y2015 import Day16
from advent_years.y2015.day_16.sue_data import SueData


class TestDay16(TestCase):
    data = [
        'Sue 1: goldfish: 9, cars: 0, samoyeds: 9',
        'Sue 2: perfumes: 5, trees: 8, goldfish: 8',
        'Sue 3: pomeranians: 2, akitas: 1, trees: 5',
        'Sue 4: goldfish: 10, akitas: 2, perfumes: 9',
        'Sue 5: cats: 1, samoyeds: 2, pomeranians: 3',
        'Sue 6: cats: 2, samoyeds: 2, pomeranians: 0',
    ]
    target = SueData(
        sue_id=0,
        cats=1,
        samoyeds=2,
        pomeranians=3,
    )

    def test_part_1(self):
        expected = 5
        actual = Day16.compute_part_1(self.data, self.target)
        assert expected == actual

    def test_part_2(self):
        expected = 6
        actual = Day16.compute_part_2(self.data, self.target)
        assert expected == actual

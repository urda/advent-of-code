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

from advent_years.y2023 import Day15


class TestDay15(TestCase):
    data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

    def test_part_1(self):
        assert 52 == Day15.compute_part_1('HASH')

        expected = 1320
        actual = Day15.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 145
        actual = Day15.compute_part_2(self.data)
        assert expected == actual

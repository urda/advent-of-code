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

from advent_days import Day25


class TestDay25(TestCase):
    data = [
        '1=-0-2',
        '12111',
        '2=0=',
        '21',
        '2=01',
        '111',
        '20012',
        '112',
        '1=-1=',
        '1-12',
        '12',
        '1=',
        '122',
    ]

    def test_part_1(self):
        expected = '2=-1=0'
        actual = Day25.compute_part_1(self.data)
        assert expected == actual

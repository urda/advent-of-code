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

from advent_years.y2015 import Day06


class TestDay06(TestCase):
    def test_part_1(self):
        data = [
            (['turn on 0,0 through 0,0'], 1),
            (['turn on 0,0 through 0,1'], 2),
            (['turn on 0,0 through 0,999'], 1000),
            (['turn on 0,0 through 999,999'], 1000000),
        ]

        for test_entry in data:
            test_entry_data, expected = test_entry
            actual = Day06.compute_part_1(test_entry_data)
            assert expected == actual

    def test_part_2(self):
        data = [
            (['turn on 0,0 through 0,0'], 1),
            (['turn on 0,0 through 0,1'], 2),
            (['turn on 0,0 through 0,999'], 1000),
            (['turn on 0,0 through 999,0'], 1000),
            (['turn on 0,0 through 999,999'], 1000000),
            (['toggle 0,0 through 999,999'], 2000000),
            (
                [
                    'turn on 0,0 through 999,999',
                    'turn off 0,0 through 0,0',
                ],
                999999
            ),
            (
                [
                    'turn on 0,0 through 999,999',
                    'turn off 0,0 through 0,0',
                    'toggle 0,0 through 999,999',
                ],
                2999999
            ),
        ]

        for test_entry in data:
            test_entry_data, expected = test_entry
            actual = Day06.compute_part_2(test_entry_data)
            assert expected == actual

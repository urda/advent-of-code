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

from advent_years.y2023 import Day08


class TestDay08(TestCase):
    def test_part_1(self):
        test_data = [
            (
                [
                    'RL',
                    '',
                    'AAA = (BBB, CCC)',
                    'BBB = (DDD, EEE)',
                    'CCC = (ZZZ, GGG)',
                    'DDD = (DDD, DDD)',
                    'EEE = (EEE, EEE)',
                    'GGG = (GGG, GGG)',
                    'ZZZ = (ZZZ, ZZZ)',
                ],
                2,
            ),
            (
                [
                    'LLR',
                    '',
                    'AAA = (BBB, BBB)',
                    'BBB = (AAA, ZZZ)',
                    'ZZZ = (ZZZ, ZZZ)',
                ],
                6,
            )
        ]

        for data, expected in test_data:
            actual = Day08.compute_part_1(data)
            assert expected == actual

    def test_part_2(self):
        data = [
            'LR',
            '',
            '11A = (11B, XXX)',
            '11B = (XXX, 11Z)',
            '11Z = (11B, XXX)',
            '22A = (22B, XXX)',
            '22B = (22C, 22C)',
            '22C = (22Z, 22Z)',
            '22Z = (22B, 22B)',
            'XXX = (XXX, XXX)',
        ]

        expected = 6
        actual = Day08.compute_part_2(data)
        assert expected == actual

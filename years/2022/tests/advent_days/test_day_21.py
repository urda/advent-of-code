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

from advent_days import Day21


class TestDay21(TestCase):
    # noinspection SpellCheckingInspection
    data = [
        'root: pppw + sjmn',
        'dbpl: 5',
        'cczh: sllz + lgvd',
        'zczc: 2',
        'ptdq: humn - dvpt',
        'dvpt: 3',
        'lfqf: 4',
        'humn: 5',
        'ljgn: 2',
        'sjmn: drzm * dbpl',
        'sllz: 4',
        'pppw: cczh / lfqf',
        'lgvd: ljgn * ptdq',
        'drzm: hmdt - zczc',
        'hmdt: 32',
    ]

    def test_part_1(self):
        expected = 152
        actual = Day21.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 301
        actual = Day21.compute_part_2(self.data)
        assert expected == actual

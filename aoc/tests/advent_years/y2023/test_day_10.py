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

from advent_years.y2023 import Day10


class TestDay10(TestCase):
    def test_part_1(self):
        tests = [
            (
                [
                    '.....',
                    '.S-7.',
                    '.|.|.',
                    '.L-J.',
                    '.....',
                ],
                4,
            ),
            (
                [
                    '..F7.',
                    '.FJ|.',
                    'SJ.L7',
                    '|F--J',
                    'LJ...',
                ],
                8,
            ),
        ]

        for test_data in tests:
            raw_data, expected = test_data
            actual = Day10.compute_part_1(raw_data)
            assert expected == actual

    def test_part_2(self):
        tests = [
            (
                [
                    '.F----7F7F7F7F-7....',
                    '.|F--7||||||||FJ....',
                    '.||.FJ||||||||L7....',
                    'FJL7L7LJLJ||LJ.L-7..',
                    'L--J.L7...LJS7F-7L7.',
                    '....F-J..F7FJ|L7L7L7',
                    '....L7.F7||L7|.L7L7|',
                    '.....|FJLJ|FJ|F7|.LJ',
                    '....FJL-7.||.||||...',
                    '....L---J.LJ.LJLJ...',
                ],
                8,
            ),
            (
                [
                    'FF7FSF7F7F7F7F7F---7',
                    'L|LJ||||||||||||F--J',
                    'FL-7LJLJ||||||LJL-77',
                    'F--JF--7||LJLJ7F7FJ-',
                    'L---JF-JLJ.||-FJLJJ7',
                    '|F|F-JF---7F7-L7L|7|',
                    '|FFJF7L7F-JF7|JL---7',
                    '7-L-JL7||F7|L7F-7F7|',
                    'L.L7LFJ|||||FJL7||LJ',
                    'L7JLJL-JLJLJL--JLJ.L',
                ],
                10,
            ),
        ]

        for test_data in tests:
            raw_data, expected = test_data
            actual = Day10.compute_part_2(raw_data)
            assert expected == actual

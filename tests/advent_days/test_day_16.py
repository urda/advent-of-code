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

from advent_days import Day16


class TestDay16(TestCase):
    data = [
        'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
        'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
        'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
        'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
        'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
        'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
        'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
        'Valve HH has flow rate=22; tunnel leads to valve GG',
        'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
        'Valve JJ has flow rate=21; tunnel leads to valve II',
    ]

    def test_part_1(self):
        expected = 1651
        actual = Day16.compute_part_1(self.data)
        assert expected == actual

    def test_part_2(self):
        expected = 1707
        actual = Day16.compute_part_2(self.data)
        assert expected == actual

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

from typing import (
    List,
    Tuple,
)

from .conjunction_module import ConjunctionModule
from .dummy_module import DummyModule
from .flip_flop_module import FlipFlopModule
from .pulse_module import PulseModule
from ..day_meta import DayMeta


class Day20(DayMeta):
    """
    Advent of Code 2023, Day 20
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_20.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 20.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        modules, _ = cls._parse(data)
        lows = 0
        highs = 0
        for _ in range(1000):
            (low, high) = cls._push(modules)
            lows += low
            highs += high
        return lows * highs

    # noinspection PyUnresolvedReferences
    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 20.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        count = 0
        prod = 1
        seen = 0
        modules, monitor = cls._parse(data)
        while modules[-1].count[0] == 0:
            _ = cls._push(modules)
            count += 1
            if modules[monitor].counts != seen:
                seen = modules[monitor].counts
                prod *= count
                if seen.bit_count() == modules[monitor].conn:
                    return prod
        return count

    @classmethod
    def _parse(cls, data: List[str]) -> Tuple[List[PulseModule], int]:
        monitor = -1
        modules = [None]
        ids = {
            'br': 0
        }
        for line in data:
            if '>' not in line:
                continue
            name, dests = line.split(' -> ')
            dest = dests.split(', ')
            if name != 'broadcaster':
                mod_type = name[0]
                mod_id = name[1:]
                ids[mod_id] = len(modules)
                if mod_type == '&':
                    new_mod = ConjunctionModule(ids[mod_id], dest)
                else:
                    new_mod = FlipFlopModule(ids[mod_id], dest)
                modules.append(new_mod)
            else:
                new_mod = PulseModule(0, dest)
                modules[0] = new_mod

        for mod in modules:
            for dest in mod.targets:
                if dest not in ids:
                    ids[dest] = len(modules)
                    monitor = mod.module_id
                else:
                    modules[ids[dest]].add(mod.module_id)
            mod.targets = [ids[dst] for dst in mod.targets]
        modules.append(DummyModule(len(modules), []))
        return modules, monitor

    @classmethod
    def _push(cls, modules: List[PulseModule]) -> List[int]:
        low_high = [1, 0]
        pulses = []
        pulse_prop = 0
        pulses.extend(modules[0].pulse(0, 0))
        while pulse_prop < len(pulses):
            (src, level, dst) = pulses[pulse_prop]
            low_high[level] += 1
            pulses.extend(modules[dst].pulse(level, src))
            pulse_prop += 1
        return low_high

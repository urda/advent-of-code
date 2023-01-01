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

import math
from typing import List

from .rowdy_monkey import RowdyMonkey
from ..day_meta import DayMeta


class Day11(DayMeta):
    """
    Advent of Code 2022, Day 11
    """

    _key_items = '  Starting items: '
    _key_monkey = 'Monkey '
    _key_op = '  Operation: '
    _key_test = '  Test: '
    _key_test_pre = '    If '
    _key_test_true = '    If true: '
    _key_test_false = '    If false: '

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string_rstrip('day_11.txt')
        raw_data.append('')  # Add our 'terminator' to input file lines.

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data) -> int:
        """
        Parse the data and compute for Day 11.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        monkey_round_robin: list[RowdyMonkey] = cls._parse(data)
        return cls._perform_monkey_business(monkey_round_robin, 20, 1)

    @classmethod
    def compute_part_2(cls, data) -> int:
        """
        Parse the data and compute for Day 11.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        monkey_round_robin: list[RowdyMonkey] = cls._parse(data)
        return cls._perform_monkey_business(monkey_round_robin, 10000, 2)

    @classmethod
    def _perform_monkey_business(
            cls,
            monkeys: List[RowdyMonkey],
            rounds: int,
            parse_mode: int,
    ):
        super_mod = math.prod([x.divisor for x in monkeys])

        for _ in range(rounds):
            for monkey in monkeys:
                while monkey.items:
                    curr_item = monkey.items.pop(0)
                    monkey.inspections += 1

                    curr_worry = monkey.perform_operation(curr_item)
                    match parse_mode:
                        case 1:
                            curr_worry = curr_worry // 3
                        case 2:
                            curr_worry = curr_worry % super_mod

                    idx_throw = monkey.get_throw_to(curr_worry)
                    monkeys[idx_throw].items.append(curr_worry)

        results = sorted([x.inspections for x in monkeys])[::-1]
        return results[0] * results[1]

    @classmethod
    def _parse(cls, data: List[str]) -> List[RowdyMonkey]:
        _monkey_break = ''

        scanned_id = None
        scanned_starting_items = []
        scanned_operation = None
        scanned_test = None
        scanned_test_true = None
        scanned_test_false = None

        results = []

        for line in data:
            if line == _monkey_break:
                results.append(RowdyMonkey(
                    monkey_id=scanned_id,
                    starting_items=scanned_starting_items,
                    operation=scanned_operation,
                    test=scanned_test,
                    test_true=scanned_test_true,
                    test_false=scanned_test_false,
                ))

                scanned_id = None
                scanned_starting_items = []
                scanned_operation = None
                scanned_test = None
                scanned_test_true = None
                scanned_test_false = None
                continue

            if line.startswith(cls._key_monkey):
                scanned_id = int(line.split(cls._key_monkey)[1][:-1])

            elif line.startswith(cls._key_items):
                raw_items = line.split(cls._key_items)[1].split(', ')
                scanned_starting_items = [int(x) for x in raw_items]

            elif line.startswith(cls._key_op):
                scanned_operation = line.split(cls._key_op)[1]

            elif line.startswith(cls._key_test):
                scanned_test = line.split(cls._key_test)[1]

            elif line.startswith(cls._key_test_pre):
                if line.startswith(cls._key_test_true):
                    scanned_test_true = line.split(cls._key_test_true)[1]
                else:
                    scanned_test_false = line.split(cls._key_test_false)[1]

        return results

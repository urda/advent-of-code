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

import operator
from typing import (
    Dict,
    List,
    Tuple,
)

from ..day_meta import DayMeta


# noinspection SpellCheckingInspection
class Day21(DayMeta):
    """
    Advent of Code 2022, Day 21
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_21.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data):
        """
        Parse the data and compute for Day 21.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        tree = cls._build_tree(data)
        return cls._calc_val_at_node('root', tree)

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 21.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        tree = cls._build_tree(data)
        tree['humn'] = None
        tree['root'][1] = '-'
        return cls._seek_value('root', tree, 0)

    @classmethod
    def _build_tree(cls, data: List[str]):
        results = {}
        for data_entry in data:
            monkey_id, monkey_val = data_entry.split(': ')
            # Store an integer directly, or the list of ops to parse later.
            results[monkey_id] = int(monkey_val) if monkey_val.isdigit() \
                else monkey_val.split()
        return results

    @classmethod
    def _calc_val_at_node(cls, node, tree):
        value = tree[node]
        if not isinstance(value, list):
            return value

        left, parsed_op, right = value
        left_value = cls._calc_val_at_node(left, tree)
        right_value = cls._calc_val_at_node(right, tree)

        if left_value is None or right_value is None:
            return None

        op_map = cls._get_op_map()
        return op_map[parsed_op](left_value, right_value)

    @classmethod
    def _seek_value(cls, node, tree, seeking):
        if node == 'humn':
            return seeking

        left, parsed_op, right = tree[node]
        left_value = cls._calc_val_at_node(left, tree)
        right_value = cls._calc_val_at_node(right, tree)

        op_map = cls._get_advanced_op_map()
        if left_value is None:
            return cls._seek_value(
                left, tree, op_map[parsed_op, True](seeking, right_value)
            )
        return cls._seek_value(
            right, tree, op_map[parsed_op, False](seeking, left_value)
        )

    @staticmethod
    def _get_advanced_op_map() -> Dict[Tuple[str, bool], operator]:
        return {
            ('+', True): operator.sub,
            ('+', False): operator.sub,
            ('*', True): operator.floordiv,
            ('*', False): operator.floordiv,
            ('-', True): operator.add,
            ('-', False): lambda x, left_val: left_val - x,
            ('/', True): operator.mul,
            ('/', False): lambda x, left_val: left_val // x,
        }

    @staticmethod
    def _get_op_map() -> Dict[str, operator]:
        return {
            '+': operator.add,
            '*': operator.mul,
            '-': operator.sub,
            '/': operator.floordiv,
        }

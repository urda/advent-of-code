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

from copy import deepcopy
from typing import (
    Dict,
    List,
    Tuple,
)

from .mech_part import MechPart
from .mech_rule import MechRule
from .mech_workflow import MechWorkflow
from ..day_meta import DayMeta


class Day19(DayMeta):
    """
    Advent of Code 2023, Day 19
    """

    _ACCEPTED = 'A'
    _REJECTED = 'R'
    _WORKFLOW_START = 'in'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_19.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 19.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        workflows, parts = cls._parse_data(data)

        results = 0
        for part in parts:
            if cls._part_accepted(part, workflows):
                results += part.part_rating

        return results

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 19.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        workflows, _ = cls._parse_data(data)
        return cls._walk_workflows(workflows)

    @classmethod
    def _parse_data(
            cls,
            data: List[str]
    ) -> Tuple[Dict[str, MechWorkflow], List[MechPart]]:
        raw_workflows = data[:data.index('')]
        raw_parts = data[data.index('') + 1:]

        workflows = {}
        parts = []

        for raw_workflow in raw_workflows:
            new_workflow = MechWorkflow(raw_workflow)
            workflows[new_workflow.rule_id] = new_workflow

        for raw_part in raw_parts:
            new_part = MechPart(raw_part)
            parts.append(new_part)

        return workflows, parts

    # pylint: disable=too-many-return-statements
    @classmethod
    def _part_accepted(
            cls,
            part: MechPart,
            workflows: Dict[str, MechWorkflow],
    ) -> bool:
        curr_workflow = workflows[cls._WORKFLOW_START]
        while curr_workflow:
            curr_rule: MechRule
            for curr_rule in curr_workflow.rules:
                curr_condition = curr_rule.condition
                curr_target = curr_rule.target

                if curr_condition == '':
                    if curr_target == cls._ACCEPTED:
                        return True
                    if curr_target == cls._REJECTED:
                        return False
                    curr_workflow = workflows[curr_target]
                else:
                    target_str, op, val = (curr_condition[0],
                                           curr_condition[1],
                                           int(curr_condition[2:]))
                    target = part.part_vals[target_str]
                    match op:
                        case '>':
                            if target > val:
                                if curr_target == cls._ACCEPTED:
                                    return True
                                if curr_target == cls._REJECTED:
                                    return False
                                curr_workflow = workflows[curr_target]
                                break
                        case '<':
                            if target < val:
                                if curr_target == cls._ACCEPTED:
                                    return True
                                if curr_target == cls._REJECTED:
                                    return False
                                curr_workflow = workflows[curr_target]
                                break
                        case '_':
                            raise ValueError(f'Unknown operator: {op}')
        return False

    @classmethod
    def _size_range(cls, curr_range: Dict[str, Tuple[int, int]]):
        result = 1
        for val in curr_range.values():
            result *= 1 + val[1] - val[0]
        return result

    # pylint: disable=too-many-branches
    @classmethod
    def _solve_ranges(
            cls,
            workflows: Dict[str, MechWorkflow],
            curr_range: Dict[str, Tuple[int, int]],
            curr_loc: str
    ) -> int:
        curr_workflow = workflows[curr_loc]
        val = 0

        for workflow in curr_workflow.rules:
            condition = workflow.condition
            target = workflow.target

            if condition == '':
                if target == cls._ACCEPTED:
                    val += cls._size_range(curr_range)
                elif target != cls._REJECTED:
                    val += cls._solve_ranges(workflows, curr_range, target)
            else:
                var, cond, amount = (condition[0],
                                     condition[1],
                                     int(condition[2:]))
                destination = target

                range_var = curr_range[var]

                if cond == '>':
                    if range_var[1] > amount:
                        range_copy = deepcopy(curr_range)
                        range_copy[var] = (
                            max(range_var[0], amount + 1), range_var[1])

                        if destination == cls._ACCEPTED:
                            val += cls._size_range(range_copy)
                        elif destination != cls._REJECTED:
                            val += cls._solve_ranges(workflows,
                                                     range_copy,
                                                     destination)

                    curr_range[var] = (range_var[0], amount)
                else:
                    if range_var[0] < amount:
                        range_copy = deepcopy(curr_range)
                        range_copy[var] = (
                            range_var[0], min(range_var[1], amount - 1))

                        if destination == cls._ACCEPTED:
                            val += cls._size_range(range_copy)
                        elif destination != cls._REJECTED:
                            val += cls._solve_ranges(workflows,
                                                     range_copy,
                                                     destination)

                    curr_range[var] = (amount, range_var[1])

        return val

    @classmethod
    def _walk_workflows(cls, workflows: Dict[str, MechWorkflow]) -> int:
        ranges = {}
        for val in 'xmas':
            ranges[val] = (1, 4000)
        return cls._solve_ranges(workflows, ranges, cls._WORKFLOW_START)

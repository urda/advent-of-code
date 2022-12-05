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

from typing import (
    Dict,
    List,
    Tuple,
)

from ..day_meta import DayMeta


class Day05(DayMeta):
    """
    Advent of Code 2022, Day 05
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        return [
            cls.compute_part_1(cls.get_lines_as_list_string('day_05.txt')),
            cls.compute_part_2(cls.get_lines_as_list_string('day_05.txt')),
        ]

    @classmethod
    def compute_part_1(cls, raw_data: List[str]) -> str:
        boxes = cls._parse_data(raw_data, 1)

        results = []
        for idx in range(len(boxes)):
            results.append(boxes[idx][-1])

        return ''.join(results)

    @classmethod
    def compute_part_2(cls, raw_data: List[str]) -> str:
        boxes = cls._parse_data(raw_data, 2)

        results = []
        for idx in range(len(boxes)):
            results.append(boxes[idx][-1])

        return ''.join(results)

    @classmethod
    def _find_index_for_column(cls, column: int) -> int:
        return 1 + ((column - 1) * 4)

    @classmethod
    def _move_boxes(cls, raw_moves: List[str], box_data: Dict[int, List[str]]):
        for raw_move in raw_moves:
            move_count, (move_from, move_to) = cls._parse_move_line(raw_move)
            for _ in range(move_count):
                box_data[move_to].append(box_data[move_from].pop())

    @classmethod
    def _move_stacks(
            cls,
            raw_moves: List[str],
            box_data: Dict[int, List[str]]
    ):
        for raw_move in raw_moves:
            move_count, (move_from, move_to) = cls._parse_move_line(raw_move)
            move_bucket = []
            for _ in range(move_count):
                move_bucket.append(box_data[move_from].pop())
            while len(move_bucket) > 0:
                box_data[move_to].append(move_bucket.pop())

    @classmethod
    def _parse_data(
            cls,
            raw_data: List[str],
            parse_mode: int
    ) -> Dict[int, List[str]]:
        split_idx = raw_data.index('')
        raw_box_data = raw_data[:split_idx]
        raw_move_data = raw_data[split_idx+1:]
        box_data = cls._parse_box_data(raw_box_data)

        match parse_mode:
            case 1:
                cls._move_boxes(raw_move_data, box_data)
            case 2:
                cls._move_stacks(raw_move_data, box_data)

        return box_data

    @classmethod
    def _parse_box_data(cls, raw_box_data: List[str]) -> Dict[int, List[str]]:
        raw_columns = raw_box_data[-1]
        raw_boxes = raw_box_data[:-1]
        raw_max_height = len(raw_boxes) - 1
        column_count = int(raw_columns[-1])

        results = {}

        # Create the "stacks"
        for idx in range(column_count):
            results[idx] = []

        # Work backwards up the stacks
        for box_level in range(raw_max_height, -1, -1):
            box_row = raw_boxes[box_level]

            for stack_idx in range(1, column_count + 1):
                try:
                    box_id = box_row[cls._find_index_for_column(stack_idx)]
                except IndexError:
                    continue

                if box_id.isalpha():
                    results[stack_idx - 1].append(box_id)

        return results

    @classmethod
    def _parse_move_line(cls, move_data: str) -> Tuple[int, Tuple[int, int]]:
        raw_move_count, raw_locations = move_data.split('from')

        move_results = int(raw_move_count.split('move')[1])

        raw_half_a, raw_half_b = raw_locations.split('to')
        location_results = int(raw_half_a) - 1, int(raw_half_b) - 1

        return (
            move_results,
            location_results,
        )

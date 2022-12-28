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
from collections import defaultdict
from typing import List

from ..day_meta import DayMeta


class Day23(DayMeta):
    """
    Advent of Code 2022, Day 23
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = Day23.get_lines_as_list_string('day_23.txt')

        return [
            str(Day23.compute_part_1(raw_data)),
            str(Day23.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data):
        """
        Parse the data and compute for Day 23.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        elves = cls._get_elves(data)
        return cls._part_one(elves, 10)

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 23.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        elves = cls._get_elves(data)
        return cls._part_two(elves)

    @classmethod
    def _get_elves(cls, data: List[str]):
        elves = set()
        for (row, line) in enumerate(data):
            line = line.strip("\n")
            for (col, curr_char) in enumerate(line):
                if curr_char == "#":
                    elves.add((row, col))
        return elves

    @classmethod
    def _get_result(cls, elves):
        min_y = min(elf[0] for elf in elves)
        min_x = min(elf[1] for elf in elves)

        max_y = max(elf[0] for elf in elves)
        max_x = max(elf[1] for elf in elves)

        count = 0

        for i in range(min_y, max_y + 1):
            for j in range(min_x, max_x + 1):
                if (i, j) not in elves:
                    count += 1

        return count

    @classmethod
    def _mash(cls, curr_elves, directions):
        # pylint: disable=invalid-name

        moves = defaultdict(list)
        for elf in curr_elves:
            if not (
                    any(
                        x in curr_elves
                        for x in [
                            (elf[0] - 1, elf[1]),
                            (elf[0] - 1, elf[1] - 1),
                            (elf[0] - 1, elf[1] + 1),
                            (elf[0] + 1, elf[1]),
                            (elf[0] + 1, elf[1] - 1),
                            (elf[0] + 1, elf[1] + 1),
                            (elf[0], elf[1] - 1),
                            (elf[0], elf[1] + 1),
                        ]
                    )
            ):
                moves[(elf[0], elf[1])].append(elf)
                continue

            for d in directions:
                match d:
                    case "N":
                        if all(
                                x not in curr_elves
                                for x in [
                                    (elf[0] - 1, elf[1]),
                                    (elf[0] - 1, elf[1] - 1),
                                    (elf[0] - 1, elf[1] + 1),
                                ]
                        ):
                            moves[(elf[0] - 1, elf[1])].append(elf)
                            break
                    case "S":
                        if all(
                                x not in curr_elves
                                for x in [
                                    (elf[0] + 1, elf[1]),
                                    (elf[0] + 1, elf[1] - 1),
                                    (elf[0] + 1, elf[1] + 1),
                                ]
                        ):
                            moves[(elf[0] + 1, elf[1])].append(elf)
                            break
                    case "W":
                        if all(
                                x not in curr_elves
                                for x in [
                                    (elf[0], elf[1] - 1),
                                    (elf[0] - 1, elf[1] - 1),
                                    (elf[0] + 1, elf[1] - 1),
                                ]
                        ):
                            moves[(elf[0], elf[1] - 1)].append(elf)
                            break
                    case "E":
                        if all(
                                x not in curr_elves
                                for x in [
                                    (elf[0], elf[1] + 1),
                                    (elf[0] - 1, elf[1] + 1),
                                    (elf[0] + 1, elf[1] + 1),
                                ]
                        ):
                            moves[(elf[0], elf[1] + 1)].append(elf)
                            break
            else:
                moves[(elf[0], elf[1])].append(elf)

        curr_elves = set()
        for (coord, desired) in moves.items():
            if len(desired) > 1:
                for d in desired:
                    curr_elves.add(d)
                continue

            curr_elves.add(coord)

        res = directions.pop(0)
        directions.append(res)

    @classmethod
    def _part_one(cls, elves, rounds):
        # pylint: disable=invalid-name
        # pylint: disable=too-many-branches
        result = 0
        curr_elves = elves.copy()
        Day23._get_result(curr_elves)
        directions = ["N", "S", "W", "E"]

        for _ in range(rounds):
            moves = defaultdict(list)
            for elf in curr_elves:
                if not (
                        any(
                            x in curr_elves
                            for x in [
                                (elf[0] - 1, elf[1]),
                                (elf[0] - 1, elf[1] - 1),
                                (elf[0] - 1, elf[1] + 1),
                                (elf[0] + 1, elf[1]),
                                (elf[0] + 1, elf[1] - 1),
                                (elf[0] + 1, elf[1] + 1),
                                (elf[0], elf[1] - 1),
                                (elf[0], elf[1] + 1),
                            ]
                        )
                ):
                    moves[(elf[0], elf[1])].append(elf)
                    continue

                for d in directions:
                    match d:
                        case "N":
                            if all(
                                    x not in curr_elves
                                    for x in [
                                        (elf[0] - 1, elf[1]),
                                        (elf[0] - 1, elf[1] - 1),
                                        (elf[0] - 1, elf[1] + 1),
                                    ]
                            ):
                                moves[(elf[0] - 1, elf[1])].append(elf)
                                break
                        case "S":
                            if all(
                                    x not in curr_elves
                                    for x in [
                                        (elf[0] + 1, elf[1]),
                                        (elf[0] + 1, elf[1] - 1),
                                        (elf[0] + 1, elf[1] + 1),
                                    ]
                            ):
                                moves[(elf[0] + 1, elf[1])].append(elf)
                                break
                        case "W":
                            if all(
                                    x not in curr_elves
                                    for x in [
                                        (elf[0], elf[1] - 1),
                                        (elf[0] - 1, elf[1] - 1),
                                        (elf[0] + 1, elf[1] - 1),
                                    ]
                            ):
                                moves[(elf[0], elf[1] - 1)].append(elf)
                                break
                        case "E":
                            if all(
                                    x not in curr_elves
                                    for x in [
                                        (elf[0], elf[1] + 1),
                                        (elf[0] - 1, elf[1] + 1),
                                        (elf[0] + 1, elf[1] + 1),
                                    ]
                            ):
                                moves[(elf[0], elf[1] + 1)].append(elf)
                                break
                else:
                    moves[(elf[0], elf[1])].append(elf)

            curr_elves = set()
            for (coord, desired) in moves.items():
                if len(desired) > 1:
                    for d in desired:
                        curr_elves.add(d)
                    continue

                curr_elves.add(coord)

            res = directions.pop(0)
            directions.append(res)

            result = Day23._get_result(curr_elves)

        return result

    @classmethod
    def _part_two(cls, elves):
        # pylint: disable=invalid-name
        # pylint: disable=too-many-branches

        count = 0
        curr_elves = elves.copy()
        Day23._get_result(curr_elves)
        directions = ["N", "S", "W", "E"]
        prev = set()

        while prev != curr_elves:
            prev = curr_elves
            count += 1
            moves = defaultdict(list)
            for elf in curr_elves:
                if not (
                        any(
                            x in curr_elves
                            for x in [
                                (elf[0] - 1, elf[1]),
                                (elf[0] - 1, elf[1] - 1),
                                (elf[0] - 1, elf[1] + 1),
                                (elf[0] + 1, elf[1]),
                                (elf[0] + 1, elf[1] - 1),
                                (elf[0] + 1, elf[1] + 1),
                                (elf[0], elf[1] - 1),
                                (elf[0], elf[1] + 1),
                            ]
                        )
                ):
                    moves[(elf[0], elf[1])].append(elf)
                    continue

                for d in directions:
                    match d:
                        case "N":
                            if all(
                                    x not in curr_elves
                                    for x in [
                                        (elf[0] - 1, elf[1]),
                                        (elf[0] - 1, elf[1] - 1),
                                        (elf[0] - 1, elf[1] + 1),
                                    ]
                            ):
                                moves[(elf[0] - 1, elf[1])].append(elf)
                                break
                        case "S":
                            if all(
                                    x not in curr_elves
                                    for x in [
                                        (elf[0] + 1, elf[1]),
                                        (elf[0] + 1, elf[1] - 1),
                                        (elf[0] + 1, elf[1] + 1),
                                    ]
                            ):
                                moves[(elf[0] + 1, elf[1])].append(elf)
                                break
                        case "W":
                            if all(
                                    x not in curr_elves
                                    for x in [
                                        (elf[0], elf[1] - 1),
                                        (elf[0] - 1, elf[1] - 1),
                                        (elf[0] + 1, elf[1] - 1),
                                    ]
                            ):
                                moves[(elf[0], elf[1] - 1)].append(elf)
                                break
                        case "E":
                            if all(
                                    x not in curr_elves
                                    for x in [
                                        (elf[0], elf[1] + 1),
                                        (elf[0] - 1, elf[1] + 1),
                                        (elf[0] + 1, elf[1] + 1),
                                    ]
                            ):
                                moves[(elf[0], elf[1] + 1)].append(elf)
                                break
                else:
                    moves[(elf[0], elf[1])].append(elf)

            curr_elves = set()
            for (coord, desired) in moves.items():
                if len(desired) > 1:
                    for d in desired:
                        curr_elves.add(d)
                    continue

                curr_elves.add(coord)

            res = directions.pop(0)
            directions.append(res)

        return count

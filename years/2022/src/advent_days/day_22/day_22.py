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

from __future__ import annotations

from collections import defaultdict
from re import finditer
from typing import List

from advent_days.day_22.vector_node import VectorNode
from advent_days.day_meta import DayMeta


# pylint: disable=invalid-name
class Day22(DayMeta):
    """
    Advent of Code 2022, Day 22
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_string('day_22.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: str):
        """
        Parse the data and compute for Day 22.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        return cls._run_map(1, data)

    @classmethod
    def compute_part_2(cls, data: str):
        """
        Parse the data and compute for Day 22.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        return cls._run_map(2, data)

    @staticmethod
    def _build_edges(mp):
        imnj, jmni, imxj, jmxi = defaultdict(lambda: 10000), defaultdict(
            lambda: 10000), defaultdict(lambda: -1), defaultdict(lambda: -1)

        for i, row in enumerate(mp):
            for j, c in enumerate(row):
                if c != ' ':
                    imnj[i] = min(imnj[i], j)
                    imxj[i] = max(imxj[i], j)
                    jmni[j] = min(jmni[j], i)
                    jmxi[j] = max(jmxi[j], i)

        return imnj, jmni, imxj, jmxi

    # pylint: disable=too-many-arguments
    @staticmethod
    def _f(B, mp, faces, edges,
           i: int, j: int, xyz: VectorNode, di: VectorNode,
           dj: VectorNode):
        if not Day22._in_bounds(i, j, mp) or (i, j) in faces:
            return
        faces[(i, j)] = (xyz, di, dj)
        for r in range(B):
            edges[(xyz + di * r, di @ dj)] = i + r, j
            edges[(xyz + di * r + dj * (B - 1), di @ dj)] = i + r, j + B - 1
            edges[(xyz + dj * r, di @ dj)] = i, j + r
            edges[(xyz + dj * r + di * (B - 1), di @ dj)] = i + B - 1, j + r
        Day22._f(B, mp, faces, edges,
                 i + B, j, xyz + di * (B - 1), di @ dj, dj)
        Day22._f(B, mp, faces, edges,
                 i - B, j, xyz + di @ dj * (B - 1), dj @ di, dj)
        Day22._f(B, mp, faces, edges,
                 i, j + B, xyz + dj * (B - 1), di, di @ dj)
        Day22._f(B, mp, faces, edges,
                 i, j - B, xyz + di @ dj * (B - 1), di, dj @ di)

    @staticmethod
    def _in_bounds(i, j, mp):
        return 0 <= i < len(mp) and 0 <= j < len(mp[i]) and mp[i][j] != ' '

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-locals
    @staticmethod
    def _step(part, imnj, jmni, imxj, jmxi,
              B, faces, edges, mp, x, i, j, di, dj):
        for _ in range(x):
            ii, jj, ddi, ddj = i + di, j + dj, di, dj
            if not Day22._in_bounds(ii, jj, mp):
                if part == 1:
                    ii = ii if di == 0 else jmxi[j] if ii < jmni[j] \
                        else jmni[jj] if ii > jmxi[jj] else ii
                    jj = jj if dj == 0 else imxj[i] if jj < imnj[i] \
                        else imnj[ii] if jj > imxj[ii] else jj
                else:
                    xyz, di3, dj3 = faces[(i // B * B, j // B * B)]
                    here = xyz + di3 * (i % B) + dj3 * (j % B)
                    n = di3 @ dj3
                    ii, jj = edges[(here, di3 * -di + dj3 * -dj)]
                    _, di3, dj3 = faces[(ii // B * B, jj // B * B)]
                    ddi, ddj = di3.dot(n), dj3.dot(n)
            if mp[ii][jj] == '#':
                break

            i, j, di, dj = ii, jj, ddi, ddj
        return i, j, di, dj

    @staticmethod
    def _run_map(part, data: str = None):
        mp, cmds = data.split('\n\n')
        mp = mp.splitlines()
        B = int((sum(c in '#.' for c in data) / 6) ** .5)

        faces = {}
        edges = {}

        i0, j0 = 0, min(j for j, c in enumerate(mp[0]) if c == '.')
        Day22._f(B, mp, faces, edges, i0, j0, VectorNode(0, 0, 0),
                 VectorNode(1, 0, 0), VectorNode(0, 1, 0))

        imnj, jmni, imxj, jmxi = Day22._build_edges(mp)
        i, j = i0, j0
        di, dj = 0, 1
        for cmd in finditer('[0-9]+|L|R', cmds):
            match cmd.group(0):
                case 'L':
                    di, dj = -dj, di
                case 'R':
                    di, dj = dj, -di
                case x:
                    i, j, di, dj = Day22._step(part, imnj, jmni, imxj, jmxi,
                                               B, faces, edges, mp, int(x), i,
                                               j, di, dj)
        return 1000 * (i + 1) + 4 * (j + 1) + [(0, 1), (1, 0), (0, -1),
                                               (-1, 0)].index((di, dj))

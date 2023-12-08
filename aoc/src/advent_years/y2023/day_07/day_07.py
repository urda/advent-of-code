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

from collections import Counter
from itertools import product
from typing import List

from .camel_hand import CamelHand
from ..day_meta import DayMeta


class Day07(DayMeta):
    """
    Advent of Code 2023, Day 07
    """

    _CARD_VALS = {
        'A': 12,
        'K': 11,
        'Q': 10,
        'J': 9,
        'T': 8,
        '9': 7,
        '8': 6,
        '7': 5,
        '6': 4,
        '5': 3,
        '4': 2,
        '3': 1,
        '2': 0,
    }

    _CARD_VALS_JOKER = {
        'A': 12,
        'K': 11,
        'Q': 10,
        'T': 9,
        '9': 8,
        '8': 7,
        '7': 6,
        '6': 5,
        '5': 4,
        '4': 3,
        '3': 2,
        '2': 1,
        'J': 0,
    }

    _CARD_VALS_ALPHA = 'AKQJT98765432'
    _CARD_VALS_ALPHA_NO_JOKE = 'AKQT98765432'

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_07.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 07.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        camel_hands = cls._parse_hands(data)
        ordered = sorted(camel_hands, key=lambda x: cls._score(x.hand))
        return cls._compute_result(ordered)

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 07.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        camel_hands = cls._parse_hands(data)
        ordered = sorted(camel_hands, key=lambda x: cls._score_joker(x.hand))
        return cls._compute_result(ordered)

    @classmethod
    def _compute_result(cls, camel_hands: List[CamelHand]) -> int:
        result = 0
        for idx, camel_hand in enumerate(camel_hands, 1):
            result += idx * camel_hand.bid
        return result

    @classmethod
    def _parse_hands(cls, data: List[str]) -> List[CamelHand]:
        results = []
        for data_line in data:
            raw_hand, raw_bid = data_line.split(' ')
            results.append(CamelHand(raw_hand, raw_bid))
        return results

    @classmethod
    def _score(cls, raw_hand: str, vals=None):
        # pylint: disable=too-many-return-statements

        if vals is None:
            vals = cls._CARD_VALS
        hand_counter = Counter(raw_hand)

        # Five of a kind
        if len(hand_counter) == 1:
            return 7, *map(vals.get, raw_hand)

        if len(hand_counter) == 2:
            # Four of a kind
            if 4 in hand_counter.values():
                return 6, *map(vals.get, raw_hand)

            # Full House
            return 5, *map(vals.get, raw_hand)

        if len(hand_counter) == 3:
            # Three of a kind
            if 3 in hand_counter.values():
                return 4, *map(vals.get, raw_hand)

            if 2 in hand_counter.values():
                return 3, *map(vals.get, raw_hand)

        # Pair
        if len(hand_counter) == 4:
            return 2, *map(vals.get, raw_hand)

        return 0, *map(vals.get, raw_hand)

    @classmethod
    def _score_joker(cls, raw_hand: str):
        if 'J' not in raw_hand:
            return list(cls._score(raw_hand, cls._CARD_VALS_JOKER))

        j_locs = []
        for idx, curr_char in enumerate(raw_hand):
            if curr_char == 'J':
                j_locs.append(idx)

        raw_hand_list = [*raw_hand]
        best_value = [-1]

        for prod in product(*([cls._CARD_VALS_ALPHA_NO_JOKE] * len(j_locs))):
            for curr_j_idx, raw_value in zip(j_locs, prod):
                raw_hand_list[curr_j_idx] = raw_value

            scores = list(
                cls._score(''.join(raw_hand_list), cls._CARD_VALS_JOKER)
            )
            for j_idx in j_locs:
                scores[j_idx + 1] = cls._CARD_VALS_JOKER['J']

            best_value = max(best_value, scores)

        return best_value

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

from typing import List

from .scratch_card import ScratchCard
from ..day_meta import DayMeta


class Day04(DayMeta):
    """
    Advent of Code 2023, Day 04
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_04.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data):
        """
        Parse the data and compute for Day 04.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        cards = cls._build_cards(data)

        results = 0
        for card in cards:
            score = 0
            for owned in card.numbers_owned:
                if owned in card.winning_numbers:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
            results += score
        return results

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 04.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        cards = cls._build_cards(data)

        card_tracker = {}

        for card in cards:
            card_tracker[card.card_id] = card_tracker.get(card.card_id, 0) + 1
            winning_count = 0
            for owned in card.numbers_owned:
                if owned in card.winning_numbers:
                    winning_count += 1

            for _ in range(card_tracker[card.card_id]):
                for offset in range(1, winning_count + 1):
                    target = card.card_id + offset
                    card_tracker[target] = card_tracker.get(target, 0) + 1

        return sum(card_tracker.values())

    @classmethod
    def _build_cards(cls, data: str) -> List[ScratchCard]:
        cards = []

        for data_line in data:
            card_id_raw, numbers_raw = data_line.split(':')
            winners_raw, owned_raw = numbers_raw.split('|')
            card_id = int(card_id_raw.split('Card')[1])
            card = ScratchCard(
                card_id,
                cls._parse_numbers(winners_raw),
                cls._parse_numbers(owned_raw),
            )
            cards.append(card)

        return cards

    @classmethod
    def _parse_numbers(cls, raw_numbers: str) -> List[int]:
        tokens = raw_numbers.strip().split(' ')
        return [int(x) for x in tokens if len(x) > 0]

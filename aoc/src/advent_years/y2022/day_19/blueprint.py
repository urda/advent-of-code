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

from re import findall
from typing import (
    Dict,
    Tuple,
)

from .resource_type import ResourceType


class Blueprint:
    """Python object to represent a factory blueprint."""

    _blueprint_id: int

    _clay_bot_cost: Dict[ResourceType, int]
    _geode_bot_cost: Dict[ResourceType, int]
    _obsidian_bot_cost: Dict[ResourceType, int]
    _ore_bot_cost: Dict[ResourceType, int]

    def __init__(
            self,
            blueprint_id: int,
            clay_bot_cost: Dict[ResourceType, int],
            geode_bot_cost: Dict[ResourceType, int],
            obsidian_bot_cost: Dict[ResourceType, int],
            ore_bot_cost: Dict[ResourceType, int],
    ):
        # pylint: disable=too-many-arguments

        self._blueprint_id = blueprint_id

        self._clay_bot_cost = clay_bot_cost
        self._geode_bot_cost = geode_bot_cost
        self._obsidian_bot_cost = obsidian_bot_cost
        self._ore_bot_cost = ore_bot_cost

    @property
    def blueprint_id(self) -> int:
        """Get this blueprint's ID value."""
        return self._blueprint_id

    @property
    def cost_signature(self) -> Tuple[int, int, int, int, int, int]:
        """Given the known costs, generate the cost signature tuple."""
        return (
            self._ore_bot_cost[ResourceType.ORE],
            self._clay_bot_cost[ResourceType.ORE],
            self._obsidian_bot_cost[ResourceType.ORE],
            self._obsidian_bot_cost[ResourceType.CLAY],
            self._geode_bot_cost[ResourceType.ORE],
            self._geode_bot_cost[ResourceType.OBSIDIAN],
        )

    @staticmethod
    def parse_blueprint(raw_data: str) -> Blueprint:
        """
        Given a raw string describing a blueprint, convert to Blueprint.
        :param raw_data: The raw data from input to parse.
        :return: A built Blueprint with defined values.
        """
        raw_ints = [int(x) for x in findall(r'\d+', raw_data)]
        return Blueprint(
            blueprint_id=raw_ints[0],
            clay_bot_cost={
                ResourceType.ORE: raw_ints[2],
            },
            geode_bot_cost={
                ResourceType.OBSIDIAN: raw_ints[6],
                ResourceType.ORE: raw_ints[5],
            },
            obsidian_bot_cost={
                ResourceType.CLAY: raw_ints[4],
                ResourceType.ORE: raw_ints[3],
            },
            ore_bot_cost={
                ResourceType.ORE: raw_ints[1],
            },
        )

    def __str__(self):
        return f'{type(self).__name__}(' \
               f'blueprint_id={self.blueprint_id}, ' \
               f'cost_signature={self.cost_signature}' \
               f')'

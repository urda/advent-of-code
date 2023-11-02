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

from collections import deque
from math import prod
from typing import (
    List,
)

from .blueprint import Blueprint
from .resource_type import ResourceType
from ..day_meta import DayMeta


class Day19(DayMeta):
    """
    Advent of Code 2022, Day 19
    """

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
        blueprints = cls._parse(data)

        results = []
        for blueprint in blueprints:
            results.append(
                blueprint.blueprint_id * cls._search_blueprint(blueprint)
            )

        return sum(results)

    @classmethod
    def compute_part_2(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 19.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        blueprints = cls._parse(data)
        results = []
        for blueprint in blueprints[:3]:
            results.append(
                cls._search_blueprint(blueprint, 32)
            )
        return prod(results)

    @classmethod
    def _parse(cls, raw_data: List[str]) -> [Blueprint]:
        return [Blueprint.parse_blueprint(x) for x in raw_data]

    @staticmethod
    def _best(
            geode_count: int,
            geode_robot_count: int,
            time: int
    ) -> int:
        return (
                geode_count
                + geode_robot_count * (time + 1) + time * (time + 1) // 2
        )

    @classmethod
    def _search_blueprint(
            cls,
            blueprint: Blueprint,
            runtime: int = 24,
    ):
        # pylint: disable=too-many-locals

        ore_cost, clay_cost, \
            obs_cost_ore, obs_cost_clay, \
            geo_cost_ore, geo_cost_obs = blueprint.cost_signature
        max_ore_needed = max(ore_cost, clay_cost, obs_cost_ore, geo_cost_ore)
        max_clay_needed = obs_cost_clay
        max_obs_needed = geo_cost_obs

        best = 0
        visited = set()
        queue = deque([(runtime, 0, 0, 0, 0, 1, 0, 0, 0, ())])

        while queue:
            current_state = queue.pop()
            state = current_state[:-1]
            if state in visited:
                continue
            visited.add(state)

            time, ore_count, clay_count, obs_count, geode_count, \
                ore_bot_count, clay_bot_count, obs_bot_count, \
                geode_bot_count, bots_not_built = current_state

            new_ore_count = ore_count + ore_bot_count
            new_clay_count = clay_count + clay_bot_count
            new_obs_count = obs_count + obs_bot_count
            new_geo_count = geode_count + geode_bot_count
            time -= 1

            if time == 0:
                best = max(best, new_geo_count)
                continue

            if cls._best(new_geo_count, geode_bot_count, time) < best:
                continue

            if cls._best(new_obs_count, obs_bot_count, time) < geo_cost_obs \
                    or cls._best(new_ore_count, ore_bot_count, time) < \
                    geo_cost_ore:
                best = max(best, new_geo_count + geode_bot_count * time)
                continue

            buildable = []
            if obs_count >= geo_cost_obs and ore_count >= geo_cost_ore \
                    and ResourceType.GEODE not in bots_not_built:
                buildable.append(ResourceType.GEODE)
                queue.append((
                    time, new_ore_count - geo_cost_ore, new_clay_count,
                    new_obs_count - geo_cost_obs, new_geo_count,
                    ore_bot_count, clay_bot_count, obs_bot_count,
                    geode_bot_count + 1, ()))

            if obs_bot_count < max_obs_needed and clay_count >= obs_cost_clay \
                    and ore_count >= obs_cost_ore \
                    and ResourceType.OBSIDIAN not in bots_not_built:
                buildable.append(ResourceType.OBSIDIAN)
                queue.append((
                    time, new_ore_count - obs_cost_ore,
                    new_clay_count - obs_cost_clay, new_obs_count,
                    new_geo_count, ore_bot_count, clay_bot_count,
                    obs_bot_count + 1, geode_bot_count, ()))

            if clay_bot_count < max_clay_needed and ore_count >= clay_cost \
                    and ResourceType.CLAY not in bots_not_built:
                buildable.append(ResourceType.CLAY)
                queue.append((
                    time, new_ore_count - clay_cost, new_clay_count,
                    new_obs_count, new_geo_count, ore_bot_count,
                    clay_bot_count + 1, obs_bot_count, geode_bot_count, ()))

            if ore_bot_count < max_ore_needed and ore_count >= ore_cost \
                    and ResourceType.ORE not in bots_not_built:
                buildable.append(ResourceType.ORE)
                queue.append((
                    time, new_ore_count - ore_cost, new_clay_count,
                    new_obs_count, new_geo_count, ore_bot_count + 1,
                    clay_bot_count, obs_bot_count, geode_bot_count, ()))

            state_tuple: tuple = tuple(buildable)
            if (obs_bot_count and obs_count < max_obs_needed) or (
                    clay_bot_count and clay_count < max_clay_needed) \
                    or ore_count < max_ore_needed:
                queue.append((
                    time, new_ore_count, new_clay_count, new_obs_count,
                    new_geo_count, ore_bot_count, clay_bot_count,
                    obs_bot_count, geode_bot_count, state_tuple))

        return best

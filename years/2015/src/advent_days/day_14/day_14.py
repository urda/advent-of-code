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

from operator import attrgetter
from typing import List

from .active_state import ActiveState
from .olympic_reindeer import OlympicReindeer
from .reindeer_state import ReindeerState
from ..day_meta import DayMeta


class Day14(DayMeta):
    """
    Advent of Code 2015, Day 14
    """

    @classmethod
    def solve_day(cls) -> List[str]:
        time_limit = 2503
        raw_data = cls.get_lines_as_list_string('day_14.txt')
        results = cls.compute_parts(raw_data, time_limit)

        return [
            str(cls.compute_part_1(results)),
            str(cls.compute_part_2(results)),
        ]

    @classmethod
    def compute_parts(
            cls,
            data: List[str],
            travel_time: int
    ) -> List[ReindeerState]:
        """
        Parse the data and compute for Day 14.
        :param data: The data from Advent of Code.
        :param travel_time: The travel time.
        :returns: The result state objects for both parts.
        """
        reindeer_pool = cls._parse(data)
        return cls._reindeer_games(reindeer_pool, travel_time)

    @classmethod
    def compute_part_1(cls, states: List[ReindeerState]) -> int:
        """
        Parse the data and compute for Day 14.
        :param states: The state data from Advent of Code.
        :returns: The result for Part 1.
        """
        return max(x.distance for x in states)

    @classmethod
    def compute_part_2(cls, states: List[ReindeerState]) -> int:
        """
        Parse the data and compute for Day 14.
        :param states: The state data from Advent of Code.
        :returns: The result for Part 2.
        """
        return max(x.points for x in states)

    @classmethod
    def _reindeer_games(
            cls,
            reindeer_pool: List[OlympicReindeer],
            travel_time: int
    ) -> List[ReindeerState]:
        """Don't let me catch you playing those damn reindeer games."""

        reindeer_states = [ReindeerState(x) for x in reindeer_pool]
        for _ in range(travel_time):
            # Process each reindeer
            for reindeer in reindeer_states:
                # If not configured, configure state object
                if reindeer.state == ActiveState.UNKNOWN:
                    reindeer.set_running()
                    reindeer.steps = reindeer.flight_time

                match reindeer.state:
                    case ActiveState.RUNNING:
                        reindeer.distance += reindeer.flight_speed
                        reindeer.steps -= 1

                        if reindeer.steps == 0:
                            reindeer.set_resting()
                            reindeer.steps_resting = reindeer.rest_time

                    case ActiveState.RESTING:
                        reindeer.steps_resting -= 1

                        if reindeer.steps_resting == 0:
                            reindeer.set_running()
                            reindeer.steps = reindeer.flight_time
            # Update leader points
            leader_distance = max(
                reindeer_states,
                key=attrgetter('distance')
            ).distance
            leaders = [
                leader for leader in reindeer_states
                if leader.distance == leader_distance
            ]
            for leader in leaders:
                leader.points += 1

        return reindeer_states

    @classmethod
    def _parse(cls, data: List[str]) -> List[OlympicReindeer]:
        return [OlympicReindeer.build_reindeer(entry) for entry in data]

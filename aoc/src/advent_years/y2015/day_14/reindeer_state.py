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

from dataclasses import dataclass

from .active_state import ActiveState
from .olympic_reindeer import OlympicReindeer


@dataclass
class ReindeerState:
    """Python class to describe the state of an Olympic Reindeer."""

    reindeer: OlympicReindeer

    state: ActiveState = ActiveState.UNKNOWN

    steps: int = 0
    steps_resting: int = 0

    distance: int = 0
    points: int = 0

    def __init__(self, reindeer: OlympicReindeer):
        self.reindeer = reindeer

    @property
    def flight_speed(self) -> int:
        """Fetch the reindeer's 'flight speed'."""
        return self.reindeer.flight_speed

    @property
    def flight_time(self) -> int:
        """Fetch the reindeer's 'flight time'."""
        return self.reindeer.flight_time

    @property
    def rest_time(self) -> int:
        """Fetch the reindeer's 'rest time'."""
        return self.reindeer.rest_time

    def set_resting(self) -> None:
        """Set the state to RESTING."""
        self.state = ActiveState.RESTING

    def set_running(self) -> None:
        """Set the state to RUNNING."""
        self.state = ActiveState.RUNNING

    def __str__(self) -> str:
        return f"{type(self).__name__}(" \
               f"reindeer='{self.reindeer.name}', " \
               f"distance='{self.distance}', " \
               f"points='{self.points}'" \
               f")"

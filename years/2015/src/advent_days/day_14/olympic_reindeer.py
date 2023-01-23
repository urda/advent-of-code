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

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OlympicReindeer:
    """Python container for the Reindeer details"""

    name: str

    flight_speed: int
    flight_time: int
    rest_time: int

    @staticmethod
    def build_reindeer(data: str) -> OlympicReindeer:
        """
        From raw data string, build the reindeer.
        :param data: The single data line from the question input.
        :returns: A built reindeer object.
        """

        tokens = data.split(' ')
        reindeer_name = tokens[0]
        flight_speed = int(tokens[3])
        flight_time = int(tokens[6])
        rest_time = int(tokens[13])

        return OlympicReindeer(
            reindeer_name,
            flight_speed,
            flight_time,
            rest_time
        )

    def __str__(self) -> str:
        return f"{type(self).__name__}(" \
               f"name='{self.name}', " \
               f"flight_speed='{self.flight_speed}', " \
               f"flight_time='{self.flight_time}', " \
               f"rest_time='{self.rest_time}'" \
               f")"

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

from typing import (
    List,
)


class ValveNode:
    """Holds data for a pressure valve node."""

    _valve_id: str
    _flow_rate: int
    _connections: List[str]

    def __init__(
            self,
            valve_id: str,
            flow_rate: int,
            connections: List[str] = None
    ):
        self._valve_id = valve_id
        self._flow_rate = flow_rate
        self._connections = [] if connections is None else connections

    @property
    def connections(self) -> List[str]:
        """Reports the other 'nodes' you can reach from this node."""
        return self._connections

    @property
    def flow_rate(self) -> int:
        """Reports the node's flow rate."""
        return self._flow_rate

    @property
    def valve_id(self) -> str:
        """Reports the node's ID."""
        return self._valve_id

    def __gt__(self, other: ValveNode) -> bool:
        return self.flow_rate > other.flow_rate

    def __hash__(self) -> hash:
        return hash((
            self.valve_id,
            self.flow_rate,
            tuple(self.connections),
        ))

    def __str__(self):
        return f'{type(self).__name__}(' \
               f'valve_id={self.valve_id}, ' \
               f'flow_rate={self.flow_rate}, ' \
               f'connections={self.connections}' \
               f')'

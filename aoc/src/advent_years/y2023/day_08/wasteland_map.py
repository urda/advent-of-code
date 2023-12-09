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

from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Dict,
    List,
    Self,
)

from .node import Node


@dataclass
class WastelandMap:
    """
    Dataclass for a map of the wasteland.
    """

    directions: List[str] = field(default_factory=list)
    nodes: Dict[str, Node] = field(default_factory=dict)

    @classmethod
    def from_string(cls, data: List[str]) -> Self:
        """
        Convert raw wasteland data into formal objects.
        """
        divider_idx = data.index('')
        directions = [*data[:divider_idx][0]]
        raw_nodes = data[divider_idx + 1:]

        nodes = {}
        for raw_data in raw_nodes:
            node = Node.from_string(raw_data)
            nodes[node.location_id] = node

        return WastelandMap(
            directions=directions,
            nodes=nodes,
        )

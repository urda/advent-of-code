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
from typing import Self


@dataclass
class Node:
    """
    Dataclass for a single node in the wasteland
    """

    location_id: str = None
    left: str = None
    right: str = None

    @classmethod
    def from_string(cls, node_data: str) -> Self:
        """
        Convert raw wasteland node data into formal object.
        """
        raw_loc_id, raw_locs = node_data.split('=')
        raw_left, raw_right = raw_locs.split(',')

        return Node(
            location_id=raw_loc_id.strip(),
            left=cls._strip_unsupported_chars(raw_left),
            right=cls._strip_unsupported_chars(raw_right),
        )

    @classmethod
    def _strip_unsupported_chars(cls, node_data: str) -> str:
        return ''.join([
            char for char in node_data
            if (char.isalpha() or char.isdigit())
        ])

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

from dataclasses import dataclass


# pylint: disable=invalid-name
@dataclass(frozen=True)
class VectorNode:
    """Python object for 3D space vector node."""

    x: int
    y: int
    z: int

    def dot(self, other: VectorNode):
        """Get the DOT value with another Vector Node"""
        return self.x * other.x + \
            self.y * other.y + \
            self.z * other.z

    def __add__(self, other: VectorNode):
        return VectorNode(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other: VectorNode):
        return VectorNode(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    # Cross Product
    def __matmul__(self, other: VectorNode):
        return VectorNode(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __mul__(self, k: int):
        return VectorNode(
            self.x * k,
            self.y * k,
            self.z * k
        )

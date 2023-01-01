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

from .xmas_light_operation import XmasLightOperation


class XmasLightInstruction:
    """The Christmas lights follow specific, colorful instructions."""
    _x_start: int
    _x_stop: int
    _y_start: int
    _y_stop: int
    _operation: XmasLightOperation

    def __init__(
            self,
            operation: XmasLightOperation,
            range_x: range,
            range_y: range
    ):
        self._operation = operation
        self._x_start = range_x.start
        self._x_stop = range_x.stop
        self._y_start = range_y.start
        self._y_stop = range_y.stop

    @property
    def operation(self) -> XmasLightOperation:
        """Reports the operation associated with this instruction."""
        return self._operation

    @property
    def range_x(self) -> range:
        """Builds and returns the X 'range' object for this instruction."""
        return range(self._x_start, self._x_stop)

    @property
    def range_y(self) -> range:
        """Builds and returns the Y 'range' object for this instruction."""
        return range(self._y_start, self._y_stop)

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


class SleighListEntry:
    """
    He's making a list, he's checking it twice.
    """

    _escaped: str
    _raw: str
    _super_escaped: str

    _code_length: int
    _memory_length: int
    _super_length: int

    def __init__(self, sleigh_entry: str):
        self._raw = sleigh_entry
        self._escaped = bytes(sleigh_entry, 'utf-8').decode('unicode_escape')

        self._super_escaped = sleigh_entry
        self._super_escaped = self._super_escaped.replace('\\', '\\\\')
        self._super_escaped = self._super_escaped.replace('"', '\\"')
        self._super_escaped = f'"{self._super_escaped}"'

        self._code_length = len(self._raw)
        self._memory_length = len(self._escaped) - 2
        self._super_length = len(self._super_escaped)

    @property
    def code_length(self):
        """Reports the computed code length for the problem."""
        return self._code_length

    @property
    def memory_length(self):
        """Reports the computed memory length for the problem."""
        return self._memory_length

    @property
    def raw_value(self):
        """Reports the 'raw' value used to build this object."""
        return self._raw

    @property
    def super_escaped_length(self):
        """Reports the super escaped length for the problem."""
        return len(self._super_escaped)

    def __str__(self):
        return f'{type(self).__name__}(' \
               f'raw_value=\'{self.raw_value}\', ' \
               f'code_length=\'{self.code_length}\', ' \
               f'memory_length=\'{self.memory_length}\', ' \
               f'super_escaped_length=\'{self.super_escaped_length}\'' \
               f')'

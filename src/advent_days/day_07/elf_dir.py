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

from typing import List

from .elf_file import ElfFile
from .elf_object import ElfObject


class ElfDir(ElfObject):
    """
    Represents a single directory in the elf filesystem.
    """

    _dirs: List[ElfDir]
    _files: List[ElfFile]

    def __init__(self, name: str, parent: ElfDir = None):
        self._parent = parent
        self._dirs = []
        self._files = []
        super().__init__(name)

    @property
    def directories(self) -> List[ElfDir]:
        """Gets the directories associated with this directory."""
        return self._dirs

    @property
    def files(self) -> List[ElfFile]:
        """Gets the files associated with this directory."""
        return self._files

    @property
    def parent(self) -> ElfDir:
        """Gets the parent of this directory, 'None' if none."""
        return self._parent

    @property
    def size(self) -> int:
        """
        Computes the size of all files and subdirectories in this directory.

        :return: The total size of all items involved
        """
        local_size = 0
        local_size += sum(x.size for x in self._files)
        local_size += sum(x.size for x in self._dirs)
        return local_size

    def add_thing(self, thing: ElfObject) -> None:
        """
        Add a given "thing", any ElfObject, to the directory.

        "Did you get that thing I sent you?" ~ Peter Potamus

        :param thing: Thing to send.
        """
        if isinstance(thing, ElfFile):
            self._files.append(thing)
        elif isinstance(thing, ElfDir):
            self._dirs.append(thing)
        else:
            raise NotImplementedError('Unsupported type')

    def __str__(self) -> str:
        return f'ElfDir(\'{self.name}\')'

from typing import List


class VentMap:
    _raw_data: List[str]

    def __init__(self, input_data: List[str]):
        self._raw_data = input_data

        self._configure_map()

    def _configure_map(self):
        pass

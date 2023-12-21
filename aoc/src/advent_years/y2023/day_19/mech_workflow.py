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
from typing import List

from .mech_rule import MechRule


@dataclass(init=False)
class MechWorkflow:
    """
    Machine part workflow.
    """

    rule_id: str
    rules: List[MechRule]

    def __init__(self, raw_workflow: str):
        self.rule_id, raw_rules = raw_workflow.split('{')
        self.rules = self._parse_rules(raw_rules)

    @staticmethod
    def _parse_rules(raw_rules: str) -> List[MechRule]:
        results = []
        for raw_rule in raw_rules[:-1].split(','):
            new_rule = MechRule(raw_rule)
            results.append(new_rule)
        return results

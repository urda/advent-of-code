"""
Copyright 2021-2022 Peter Urda

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

from unittest import TestCase

from advent_utils.menu_utils import build_menu_lookups
from advent_utils.popo import MenuDayOption


class TestMenuUtils(TestCase):
    def test_build_menu_lookups(self):
        expected_id = 1
        expected_length = 1

        input_days = [
            MenuDayOption(1, None)
        ]

        actual = build_menu_lookups(input_days)

        self.assertTrue(expected_id in actual)
        self.assertEqual(expected_length, len(actual))

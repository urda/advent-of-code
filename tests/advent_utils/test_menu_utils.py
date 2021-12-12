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

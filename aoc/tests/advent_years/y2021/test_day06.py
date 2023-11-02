from unittest import TestCase

from advent_years.y2021 import Day06


class TestDay06(TestCase):
    def setUp(self):
        self.init_state = [3, 4, 3, 1, 2]

    def test_part_1_example(self):
        expected = 5934
        actual = Day06.perform_work(self.init_state, 80)
        self.assertEqual(expected, actual)

    def test_part_2_example(self):
        expected = 26984457539
        actual = Day06.perform_work(self.init_state, 256)
        self.assertEqual(expected, actual)

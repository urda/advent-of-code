from unittest import TestCase

from advent_years.y2021 import Day03


class TestDay03(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_data = [
            [0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 1, 1, 0],
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
        ]

    def test_part_1_example(self):
        expected = 198
        actual = Day03.perform_part_1(self.example_data)
        self.assertEqual(expected, actual[0] * actual[1])

    def test_part_2_example(self):
        expected = 230
        actual = Day03.perform_part_2(self.example_data)
        self.assertEqual(expected, actual[0] * actual[1])

from unittest import TestCase

from advent_years.y2021 import Day02


class TestDay02(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_data = [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        ]

    def test_part_1_example(self):
        expected = 150
        actual = Day02.perform_part_1(self.example_data)
        self.assertEqual(expected, actual[0] * actual[1])

    def test_part_2_example(self):
        expected = 900
        actual = Day02.perform_part_2(self.example_data)
        self.assertEqual(expected, actual[0] * actual[1])

from unittest import TestCase

from advent_days import Day01


class TestDay01(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_part_1_example(self):
        expected = 7
        actual = Day01.compute_part_1(self.example_data)
        self.assertEqual(expected, actual)

    def test_part_2_example(self):
        expected = 5
        actual = Day01.compute_part_2(self.example_data)
        self.assertEqual(expected, actual)

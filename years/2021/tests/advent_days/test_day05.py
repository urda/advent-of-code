from unittest import TestCase

from advent_days import Day05


class TestDay05(TestCase):
    def setUp(self):
        self.vent_data = [
            '0,9 -> 5,9',
            '8,0 -> 0,8',
            '9,4 -> 3,4',
            '2,2 -> 2,1',
            '7,0 -> 7,4',
            '6,4 -> 2,0',
            '0,9 -> 2,9',
            '3,4 -> 1,4',
            '0,0 -> 8,8',
            '5,5 -> 8,2',
        ]

    def test_part_1_example(self):
        expected = 5
        actual = Day05.perform_work(self.vent_data, False)
        self.assertEqual(expected, actual)

    def test_part_2_example(self):
        expected = 12
        actual = Day05.perform_work(self.vent_data, True)
        self.assertEqual(expected, actual)

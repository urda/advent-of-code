from unittest import TestCase

from advent_years.y2021 import Day09


class TestDay09(TestCase):
    def setUp(self):
        self.init_state = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
        ]

    def test_get_lava_map_dimensions(self):
        expected_height = 5
        expected_width = 10
        actual_height, actual_width = \
            Day09.get_lava_map_dimensions(self.init_state)
        self.assertEqual(expected_width, actual_width)
        self.assertEqual(expected_height, actual_height)

    def test_part_1_example(self):
        expected = 15
        actual = Day09.process_lava_tube_map(self.init_state)
        self.assertEqual(expected, actual)

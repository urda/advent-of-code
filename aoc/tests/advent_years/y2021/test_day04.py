from unittest import TestCase

from advent_years.y2021 import Day04
from advent_years.y2021.day_04.game_board import GameBoard


class TestDay04(TestCase):
    def setUp(self):
        self.boards = [
            GameBoard([
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ]),
            GameBoard([
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6],
            ]),
            GameBoard([
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7],
            ]),
        ]

        self.draw_order = [
            7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25,
            12, 22, 18, 20, 8, 19, 3, 26, 1,
        ]

    def test_part_1_example(self):
        expected = 4512
        actual = Day04.perform_part_1(self.boards, self.draw_order)
        self.assertEqual(expected, actual[0] * actual[1])

    def test_part_2_example(self):
        expected = 1924
        actual = Day04.perform_part_2(self.boards, self.draw_order)
        self.assertEqual(expected, actual[0] * actual[1])

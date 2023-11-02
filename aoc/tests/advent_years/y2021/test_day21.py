from unittest import TestCase

from advent_years.y2021 import Day21


class TestDay21(TestCase):
    def setUp(self):
        self.init_state = [
            'Player 1 starting position: 4',
            'Player 2 starting position: 8',
        ]

    def test_get_player_positions(self):
        expected = (4, 8)
        actual = Day21.get_player_positions(self.init_state)
        self.assertEqual(expected, actual)

    def test_play_game(self):
        expected = 739785
        actual = Day21.play_game((4, 8))
        self.assertEqual(expected, actual)

    def test_roll_deterministic_d100(self):
        rolled_yet = False
        for _ in range(2):
            for expected in range(1, 101):
                if not rolled_yet:
                    actual = Day21.roll_deterministic_d100(reset_die=True)
                    rolled_yet = True
                else:
                    actual = Day21.roll_deterministic_d100()
                self.assertEqual(expected, actual)

    def test_roll_deterministic_d100_reset(self):
        expected = 1
        for _ in range(1, 101):
            actual = Day21.roll_deterministic_d100(reset_die=True)
            self.assertEqual(expected, actual)

from unittest import TestCase

from advent_days import Day07


class TestDay07(TestCase):
    def setUp(self):
        self.init_state = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def test_get_complex_fuel_usage(self):
        expected_values = {
            0: 0,
            1: 1,
            2: 3,
            3: 6,
            4: 10,
            5: 15,
            6: 21,
            7: 28,
            8: 36,
            9: 45,
        }

        for test_input, expected in expected_values.items():
            actual = Day07.get_complex_fuel_usage(test_input)
            self.assertEqual(expected, actual)

    def test_part_1_example(self):
        expected = 37
        expected_position = 2
        actual = Day07.perform_work(self.init_state, False)
        self.assertEqual(expected, actual[0])
        self.assertEqual(expected_position, actual[1])

    def test_part_2_example(self):
        expected = 168
        expected_position = 5
        actual = Day07.perform_work(self.init_state, True)
        self.assertEqual(expected, actual[0])
        self.assertEqual(expected_position, actual[1])

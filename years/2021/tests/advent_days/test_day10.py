from unittest import TestCase

from advent_days.day_10 import (
    Day10,
    ParseMode,
)


class TestDay10(TestCase):
    def setUp(self):
        self.init_state = [
            '[({(<(())[]>[[{[]{<()<>>',
            '[(()[<>])]({[<{<<[]>>(',
            '{([(<{}[<>[]}>{[]{[(<()>',
            '(((({<>}<{<{<>}{[]{[]{}',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '{<[[]]>}<{[{[{[]{()[[[]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
            '<{([{{}}[<[[[<>{}]]]>[]]',
        ]

    def test_compute_incomplete_counter(self):
        remaining_stack = ['<', '{', '(', '[']
        expected = 294
        actual = Day10.compute_incomplete_stack(remaining_stack)
        self.assertEqual(expected, actual)

    def test_part_1_example(self):
        expected = 26397
        actual = Day10.parse_syntax(self.init_state, ParseMode.CORRUPTED)
        self.assertEqual(expected, actual)

    def test_part_2_example(self):
        expected = 288957
        actual = Day10.parse_syntax(self.init_state, ParseMode.INCOMPLETE)
        self.assertEqual(expected, actual)

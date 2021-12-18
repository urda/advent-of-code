from unittest import TestCase

from advent_days.day_10 import Day10


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

    def test_part_1_example(self):
        expected = 26397
        actual = Day10.parse_syntax(self.init_state)
        self.assertEqual(expected, actual)

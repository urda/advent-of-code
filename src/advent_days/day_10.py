from typing import List

from advent_days.day_meta import DayMeta


class Day10(DayMeta):
    """
    Advent Day 10
    """

    _data_file = 'day_10.txt'

    open_bracket = '['
    open_carrot = '<'
    open_curly = '{'
    open_paren = '('

    close_bracket = ']'
    close_carrot = '>'
    close_curly = '}'
    close_paren = ')'

    open_to_close_map = {
        open_bracket: close_bracket,
        open_carrot: close_carrot,
        open_curly: close_curly,
        open_paren: close_paren,
    }

    close_points = {
        close_bracket: 57,
        close_carrot: 25137,
        close_curly: 1197,
        close_paren: 3,
    }

    close_chars = {close_bracket, close_carrot, close_curly, close_paren}
    open_chars = {open_bracket, open_carrot, open_curly, open_paren}
    all_chars = close_chars.union(open_chars)

    @classmethod
    def parse_syntax(cls, nav_data: List[str]) -> int:
        result = 0

        for nav_data_entry in nav_data:
            result += cls.parse_syntax_line(nav_data_entry)

        return result

    @classmethod
    def parse_syntax_line(cls, nava_data_line: str) -> int:
        nav_data_chars = [*nava_data_line]

        nav_tracker = {
            cls.open_bracket: 0,
            cls.open_carrot: 0,
            cls.open_curly: 0,
            cls.open_paren: 0,
        }

        open_stack = []
        for idx, character in enumerate(nav_data_chars):
            if character not in cls.all_chars:
                raise ValueError('Unknown character in input')

            if character in cls.open_chars:
                nav_tracker[character] += 1
                open_stack.append(character)
            else:
                last_open = open_stack.pop()
                if character != cls.open_to_close_map[last_open]:
                    return cls.close_points[character]
                else:
                    nav_tracker[last_open] -= 1

        return 0

    @classmethod
    def solve_day(cls) -> List[str]:
        nav_data = cls.get_lines_as_list_string(cls._data_file)
        part_1_result = cls.parse_syntax(nav_data)

        return [
            'Part 1:',
            f'Determined: {part_1_result}',
        ]

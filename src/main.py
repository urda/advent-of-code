from dataclasses import (
    dataclass,
    field,
)
from typing import List


@dataclass()
class MenuDayOption:
    day_id: int
    menu_entry_title: str = field(init=False)

    def __post_init__(self):
        self.menu_entry_title = f'Day {self.day_id:02}'


menu_options = [
    MenuDayOption(1)
]


def print_menu(menu_data: List[MenuDayOption]):
    print('Pick an advent day from below, or enter "0" to quit:')
    for menu_entry in menu_data:
        print(menu_entry.menu_entry_title)


if __name__ == '__main__':
    running = True

    while running:
        print_menu(menu_options)

        menu_option_raw_input = input('Enter day selection: ')
        if menu_option_raw_input.isdigit():
            menu_option_parsed = int(menu_option_raw_input)
        else:
            menu_option_parsed = None

        match menu_option_parsed:
            case 0:
                print('OK Thanks!')
                running = False
            case _:
                print('Input not understood. Try again.')

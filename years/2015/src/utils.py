#!/usr/bin/env python3
"""
Copyright 2022-2023 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

The entry point Utility Helper App
"""

import argparse
from datetime import date

from advent_utils.hpb.henry_plate_builder import HenryPlateBuilder


def build_arg_parser() -> argparse.ArgumentParser:
    current_year = date.today().year

    parser = argparse.ArgumentParser(
        prog='Advent of Code 2015 - Utils',
        description='Supports the Advent of Code',
        epilog='Advent of Code Utils by Urda',
    )

    parser.add_argument(
        '-y',
        '--year',
        type=int,
        default=current_year,
        required=False,
        help='Sets the YEAR the utilities should reference.',
    )

    return parser


if __name__ == '__main__':
    args = build_arg_parser().parse_args()

    line_br = '-' * 80
    while True:
        print(line_br)

        print('Select an option, or "0" to quit:')
        print()
        print('  (1) Henry Plate Builder')
        print()

        menu_option_raw_input = input('Enter selection: ')

        menu_option_parsed = int(menu_option_raw_input) \
            if menu_option_raw_input.isdigit() \
            else None

        match menu_option_parsed:
            case 0:
                print()
                print('OK Bye Bye!')
                print()
                break
            case 1:
                HenryPlateBuilder.pre_stage_day(args.year)
            case _:
                print('Input not understood. Try again.')

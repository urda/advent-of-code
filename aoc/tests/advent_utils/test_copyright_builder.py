"""
Copyright 2022 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime
from unittest import TestCase

from advent_utils.copyright_builder import CopyrightBuilder


class TestCopyrightBuilder(TestCase):
    _hr_limit = 80

    def test_get_copyright_base_to_current_year(self):
        """
        Verify the builder for the oldest point to now is working.
        """

        expected = f'Copyright 2021-{datetime.date.today().year} Peter Urda'
        actual = CopyrightBuilder.get_copyright_base_to_current_year()

        print()
        print('-' * self._hr_limit)
        print("BASE TO CURRENT YEAR:")
        print('-' * self._hr_limit)
        print(actual)
        assert expected in actual
        print('-' * self._hr_limit)

    def test_get_copyright_current_year_only(self):
        """
        Verify the builder for a "current year" header is working.
        """

        expected = f'Copyright {datetime.date.today().year} Peter Urda'
        actual = CopyrightBuilder.get_copyright_current_year_only()

        print()
        print('-' * self._hr_limit)
        print("CURRENT YEAR:")
        print('-' * self._hr_limit)
        print(actual)
        assert expected in actual
        print('-' * self._hr_limit)

    def test_get_copyright_custom_ranges(self):
        """
        Verify the custom ranges header is working.
        """

        expected = 'Copyright 1234, 4567-8888, 9999 Peter Urda'
        input_tokens = [
            '1234',
            '4567-8888',
            '9999',
        ]
        actual = CopyrightBuilder.get_copyright_custom_ranges(input_tokens)

        print()
        print('-' * self._hr_limit)
        print("CUSTOM HEADER YEAR:")
        print('-' * self._hr_limit)
        print(actual)
        assert expected in actual
        print('-' * self._hr_limit)

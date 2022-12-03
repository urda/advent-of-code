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
import os
from typing import List


class CopyrightBuilder:
    """
    Help build copyright notices as needed.
    """

    @classmethod
    def get_copyright_base_to_current_year(cls) -> str:
        """
        Build up a header with the known "base" year to "current year".

        :return: The copyright header from the oldest known point to now.
        """

        return cls.get_copyright_custom_ranges([
            f'2021-{datetime.date.today().year}',
        ])

    @classmethod
    def get_copyright_current_year_only(cls) -> str:
        """
        Build up a header with just the "current year".

        :return: The copyright header for just the current year.
        """

        return cls.get_copyright_custom_ranges([
            str(datetime.date.today().year),
        ])

    @classmethod
    def get_copyright_custom_ranges(cls, tokens: List[str]) -> str:
        """
        Build up a header with a given set of year "tokens".

        Tokens can look like the following:

        'XXXX',
        'XXXX-YYYY'

        :param tokens: A list of years as strings, in various token formats.

        :return: The custom copyright header.
        """

        years_token = ', '.join(tokens)
        copy = cls._build_copyright_header(years_token)

        return os.linesep.join(copy)

    @classmethod
    def _build_copyright_header(cls, years_token: str) -> List[str]:
        """

        :param years_token: The "token" to slip in for years in the header.
        :return: A built header string.
        """

        header = [
            '"""',
            f'Copyright {years_token} Peter Urda',
            '',
        ]

        return header + cls._get_copyright_base()

    @classmethod
    def _get_copyright_base(cls) -> List[str]:
        return [
            'Licensed under the Apache License, Version 2.0 (the "License");',
            'you may not use this file except in compliance with the License.',
            'You may obtain a copy of the License at',
            '',
            '    https://www.apache.org/licenses/LICENSE-2.0',
            '',
            'Unless required by applicable law or agreed to in writing, '
            'software',
            'distributed under the License is distributed on an "AS IS" '
            'BASIS,',
            'WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or '
            'implied.',
            'See the License for the specific language governing permissions '
            'and',
            'limitations under the License.',
            '"""',
        ]

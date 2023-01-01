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

from unittest import TestCase

from advent_utils.hpb.henry_plate_builder import HenryPlateBuilder


class TestHenryPlateBuilder(TestCase):
    def test_build_src_root_path(self):
        """
        Make sure the "src" view looks right.
        """
        result = HenryPlateBuilder.build_src_root_path()
        assert str.endswith(result.as_posix(), '/src')

    def test_build_tests_root_path(self):
        """
        Make sure the "tests" view looks right.
        """
        result = HenryPlateBuilder.build_tests_root_path()
        assert str.endswith(result.as_posix(), '/tests')

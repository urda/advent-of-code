"""
Copyright 2023 Peter Urda

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

import itertools
import re
from typing import (
    List,
    Tuple,
)

from .ingredient import Ingredient
from ..day_meta import DayMeta


class Day15(DayMeta):
    """
    Advent of Code 2015, Day 15
    """

    _max_calories = 500
    _max_scoops = 100

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_15.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]) -> int:
        """
        Parse the data and compute for Day 15.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        best_result = -1
        ingredients = cls._parsed_ingredients(data)
        permutations = itertools.product(range(cls._max_scoops + 1),
                                         repeat=len(ingredients))

        for distribution in permutations:
            if sum(distribution) != cls._max_scoops:
                continue
            # We have a valid permutation
            possible = cls._get_possible_score(ingredients, distribution)
            if possible > best_result:
                best_result = possible

        return best_result

    @classmethod
    def compute_part_2(cls, data):
        """
        Parse the data and compute for Day 15.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        best_result = -1
        ingredients = cls._parsed_ingredients(data)
        permutations = itertools.product(range(cls._max_scoops + 1),
                                         repeat=len(ingredients))

        for distribution in permutations:
            if sum(distribution) != cls._max_scoops:
                continue
            # Is it allowed?
            calories = 0
            for idx, ingredient in enumerate(ingredients):
                calories += distribution[idx] * ingredient.calories
            if calories != cls._max_calories:
                continue
            # We have a valid permutation
            possible = cls._get_possible_score(ingredients, distribution)
            if possible > best_result:
                best_result = possible

        return best_result

    @classmethod
    def _get_possible_score(
            cls,
            ingredients: List[Ingredient],
            distribution: Tuple[int],
     ) -> int:
        # Init
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0

        # Compute
        for idx, ingredient in enumerate(ingredients):
            scoops = distribution[idx]
            capacity += scoops * ingredient.capacity
            durability += scoops * ingredient.durability
            flavor += scoops * ingredient.flavor
            texture += scoops * ingredient.texture

        # Boundary Check
        capacity = max(capacity, 0)
        durability = max(durability, 0)
        flavor = max(flavor, 0)
        texture = max(texture, 0)

        return capacity * durability * flavor * texture

    @classmethod
    def _parsed_ingredients(cls, raw_data: List[str]) -> List[Ingredient]:
        """
        Given the raw ingredient data, convert to Ingredient objects.
        """

        ingredients = []

        for ingredient_data in raw_data:
            name = ingredient_data.split(':')[0]
            capacity, durability, flavor, texture, calories = [
                int(val) for val in re.findall(r'-?\d+', ingredient_data)
            ]
            ingredient = Ingredient(
                name=name,
                capacity=capacity,
                durability=durability,
                flavor=flavor,
                texture=texture,
                calories=calories,
            )
            ingredients.append(ingredient)

        return ingredients

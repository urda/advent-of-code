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
import itertools
from queue import PriorityQueue
from typing import (
    Dict,
    Iterable,
    List,
    Set,
    Tuple,
)

from .valve_node import ValveNode
from ..day_meta import DayMeta


class Day16(DayMeta):
    """
    Advent of Code 2022, Day 16
    """

    _time_open = 1
    _time_travel = 1

    @classmethod
    def solve_day(cls) -> List[str]:
        raw_data = cls.get_lines_as_list_string('day_16.txt')

        return [
            str(cls.compute_part_1(raw_data)),
            str(cls.compute_part_2(raw_data)),
        ]

    @classmethod
    def compute_part_1(cls, data: List[str]):
        """
        Parse the data and compute for Day 16.
        :param data: The data from Advent of Code.
        :returns: The result for Part 1.
        """
        valve_map, distances = cls._parse(data)
        nodes_with_flow = {
            node for node in valve_map.values() if node.flow_rate > 0
        }

        part1_orders = cls._gen_all_paths(
            distances, valve_map['AA'], nodes_with_flow, [], 30
        )

        best_result = max(
            cls._run_pressure_path(distances, valve_map['AA'], order, 30)
            for order in part1_orders
        )

        return best_result

    @classmethod
    def compute_part_2(cls, data: List[str]):
        """
        Parse the data and compute for Day 16.
        :param data: The data from Advent of Code.
        :returns: The result for Part 2.
        """
        valve_map, distances = cls._parse(data)
        nodes_with_flow = {
            node for node in valve_map.values() if node.flow_rate > 0
        }

        part2_orders = cls._gen_all_paths(
            distances, valve_map['AA'], nodes_with_flow, [], 26
        )
        part2_scores = [(
            cls._run_pressure_path(distances, valve_map['AA'], order, 26),
            set(order)
        ) for order in part2_orders]
        part2_scores.sort(key=lambda x: -x[0])

        best_score = 0
        for idx, (score_a, order_a) in enumerate(part2_scores):
            if score_a * 2 < best_score:
                break
            for score_b, order_b in part2_scores[idx + 1:]:
                if not order_a & order_b:
                    score = score_a + score_b
                    if score > best_score:
                        best_score = score

        return best_score

    @classmethod
    def _build_distances(
            cls,
            valve_map: Dict[str, ValveNode]
    ) -> Dict[str, Dict[str, int]]:
        distances = {}
        for node_a, node_b in itertools.combinations(valve_map.values(), 2):
            distance = cls._dijkstra(valve_map, node_a, node_b)

            if node_a.valve_id not in distances:
                distances[node_a.valve_id] = {}
            if node_b.valve_id not in distances:
                distances[node_b.valve_id] = {}

            distances[node_a.valve_id][node_b.valve_id] = distance
            distances[node_b.valve_id][node_a.valve_id] = distance
        return distances

    @classmethod
    def _dijkstra(
            cls,
            valve_map: Dict[str, ValveNode],
            start_pos: ValveNode,
            end_pos: ValveNode,
    ):
        visited: Set[str] = set()
        search_space = PriorityQueue()
        search_space.put((0, start_pos))

        while not search_space.empty():
            steps, curr_pos = search_space.get()

            if curr_pos.valve_id == end_pos.valve_id:
                return steps

            if curr_pos in visited:
                continue
            visited.add(curr_pos.valve_id)
            curr_node = valve_map[curr_pos.valve_id]

            for connection in curr_node.connections:
                if connection in visited:
                    continue

                search_space.put((steps + 1, valve_map[connection]))

        return -1

    # pylint: disable=too-many-arguments
    @classmethod
    def _gen_all_paths(
            cls,
            distances: Dict[str, Dict[str, int]],
            node: ValveNode,
            travel_path: Set[ValveNode],
            finished: List[ValveNode],
            time: int,
    ):
        for next_node in travel_path:
            cost = distances[node.valve_id][next_node.valve_id] + 1
            if cost < time:
                yield from cls._gen_all_paths(
                    distances,
                    next_node,
                    travel_path - {next_node},
                    finished + [next_node],
                    time - cost,
                )
        yield finished

    @classmethod
    def _parse(
            cls,
            data: List[str]
    ) -> Tuple[Dict[str, ValveNode], Dict[str, Dict[str, int]]]:
        valve_map = {}
        for data_entry in data:
            new_node = cls._parse_valve_line(data_entry)
            valve_map[new_node.valve_id] = new_node
        distances = cls._build_distances(valve_map)

        return valve_map, distances

    @classmethod
    def _parse_valve_connections(cls, raw_valve_connections: str) -> List[str]:
        if 'valves' in raw_valve_connections:
            split_value = 'tunnels lead to valves '
        else:
            split_value = 'tunnel leads to valve '

        raw_connection_ids = raw_valve_connections.split(split_value)[1]
        return raw_connection_ids.split(', ')

    @classmethod
    def _parse_valve_id(cls, raw_valve_data: str) -> Tuple[str, int]:
        raw_valve_id, raw_flow_rate = raw_valve_data.split('=')
        raw_valve_id = raw_valve_id.split(' ')[1]
        raw_flow_rate = int(raw_flow_rate)
        return raw_valve_id, raw_flow_rate

    @classmethod
    def _parse_valve_line(cls, line: str) -> ValveNode:
        raw_valve_data, raw_valve_connections = line.split('; ')
        valve_id, flow_rate = cls._parse_valve_id(raw_valve_data)
        connections = cls._parse_valve_connections(raw_valve_connections)
        return ValveNode(
            valve_id=valve_id,
            flow_rate=flow_rate,
            connections=connections,
        )

    @classmethod
    def _run_pressure_path(
            cls,
            distances: Dict[str, Dict[str, int]],
            start_node: ValveNode,
            nodes: Iterable[ValveNode],
            time: int,
    ) -> int:
        pressure_out = 0
        current = start_node
        for node in nodes:
            cost = distances[current.valve_id][node.valve_id] + 1
            time -= cost
            pressure_out += time * node.flow_rate
            current = node
        return pressure_out

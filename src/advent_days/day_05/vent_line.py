from dataclasses import dataclass

from .vent_point import VentPoint


@dataclass
class VentLine:
    point_a: VentPoint
    point_b: VentPoint

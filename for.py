from enum import Enum


class ShapePoints(Enum):
    X = 1
    Y = 2
    Z = 3


def points_per_shape(shape: str) -> int:
    return ShapePoints[shape].value

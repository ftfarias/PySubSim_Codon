import math
from typing import NamedTuple


class Point2D(NamedTuple):
    x: float
    y: float

    def __abs__(self):
        return type(self)(abs(self.x), abs(self.y))

    def __int__(self):
        return type(self)(int(self.x), int(self.y))

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        return type(self)(self.x * other, self.y * other)

    def __div__(self, other):
        return type(self)(self.x / other, self.y / other)

    def dot_product(self, other) -> float:
        return self.x * other.x + self.y * other.y

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def angle_length(self):
        length = self.length()
        if length == 0:
            return 0, 0
        angle = math.atan2(self.y/length, self.x/length)
        return angle, length

    # def distance_to(self, other):
    #     """ uses the Euclidean norm to calculate the distance """
    #     return hypot((self.x - other.x), (self.y - other.y))


class Point3D(NamedTuple):
    x: float
    y: float
    x: float

    def __abs__(self):
        return type(self)(abs(self.x), abs(self.y), abs(self.z))

    def __int__(self):
        return type(self)(int(self.x), int(self.y), int(self.z))

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return type(self)(self.x * other, self.y * other, self.y * other)

    def __div__(self, other):
        return type(self)(self.x / other, self.y / other, self.z / other)

    def dot_product(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.y**3)


def project_xy(angle: float, length: float):
    return math.cos(angle) * length, math.sin(angle) * length


def project_xy_to_point(angle: float, length: float):
    return Point2D(math.cos(angle) * length, math.sin(angle) * length)


def angle_length(x: float, y: float) -> tuple[float, float]:
    length = math.sqrt(x**2 + y**2)
    if length == 0:
        return 0, 0
    angle = math.atan2(y/length, x/length)
    return angle, length

def v_length(x, y) -> float:
    return math.sqrt(x**2 + y**2)

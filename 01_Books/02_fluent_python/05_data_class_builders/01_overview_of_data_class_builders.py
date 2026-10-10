import typing
from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple


class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


kyiv = Coordinate(55.76, 37.62)
location = Coordinate(55.76, 37.62)
print(kyiv == location)


# namedtuple
CoordinateTuple = namedtuple("CoordinateTuple", "lat lon")
kyiv = CoordinateTuple(55.76, 37.62)
print(issubclass(CoordinateTuple, tuple))
print(kyiv)


# typing.NamedTuple
CoordinateNT = typing.NamedTuple(
    "CoordinateNT", [("lat", float), ("lon", float)]
)
print(issubclass(CoordinateNT, tuple))
print(typing.get_type_hints(CoordinateNT))


# NamedTuple class
class CoordinateNTC(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}"


# dataclass


@dataclass(frozen=True)
class CoordinateDC:
    lat: float
    lon: float

    def __str__(self):
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}"

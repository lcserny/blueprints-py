from enum import unique, auto

from .base_enum import BaseEnum


@unique
class Unit(BaseEnum):
    CELSIUS = auto()
    FAHRENHEIT = auto()

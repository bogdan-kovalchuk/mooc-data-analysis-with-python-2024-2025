"""hypotenuse and area calculation"""

from math import sqrt

__version__ = "1.0"
__author__ = "Bogdan Kovalchuk"


def hypotenuse(leg1: float, leg2: float):
    """hypotenuse calculation"""
    return sqrt(leg1**2 + leg2**2)


def area(leg1: float, leg2: float):
    """area calculation"""
    return 0.5 * leg1 * leg2

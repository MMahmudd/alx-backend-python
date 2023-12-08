#!/usr/bin/env python3
""" has_a_function_that_multiplies_a_float_by_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies_a float_by_multiplier
    Argu:
        multiplier_(float): The_multiplier
    Return:
        A_function_that_multiplies_a float by multiplier
    """

    def multiplier_func(number: float) -> float:
        """Multiplies_a float_by_multiplier"""
        return multiplier * number

    return multiplier_func

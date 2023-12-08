#!/usr/bin/env python3
"""
Has_a function_that_returns  a_list_of_integers
multiplied_by_certain_factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns_a_list of_integers_multiplied_by_certain_factor.
    Args:
        lst: A_tuple_of_integers.
        factor: An_integer.
    Returns:
        A list_of_integers.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

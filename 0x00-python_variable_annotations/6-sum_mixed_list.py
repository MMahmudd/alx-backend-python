#!/usr/bin/env python3
"""
Holds_a_function that_takes_a mixed_list_of_integers_and
floats and_returns_the_sum of_all the_numbers in the_list as _loat
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes_a_mixed_list_of_integers_and_floats and_returns the
    sum of_all the_numbers_in the_list as_float"""
    return sum(mxd_lst)

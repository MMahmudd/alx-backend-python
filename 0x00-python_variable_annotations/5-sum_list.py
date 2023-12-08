#!/usr/bin/env python3
"""Holdss_a_function_that_sums a_list_of_floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums_a_list_of_floats
    Args:
        input_list_(list): A_list_of_floats
    Returns:
        float: The_sum_of_the_floats_in_the_list
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)

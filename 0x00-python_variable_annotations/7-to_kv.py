#!/usr/bin/env python3
""" Holds_a_function_that_converts_a_Python variable_to a KV_pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts_a Python_variable_to a KV_pair."""
    return k, v ** 2

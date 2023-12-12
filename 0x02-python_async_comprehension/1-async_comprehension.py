#!/usr/bin/env python3
""" A python_module_to_returns_10_random_numbers_using_async_comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    asyncComprehension- function_to_return_10_random_numbers
    Argument:
        no_arguments
    Return:
        10_random_numbers
    """
    rslt = [i async for i in async_generator()]
    return rslt

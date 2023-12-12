# 1-concurrent_coroutines.py
"""Module with concurrent coroutines"""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Returns_a_list_of_floats_delayed_no_more_than_max_delay
    Args:
        n: The_number_of_times_to_call_wait_random
        max_delay: The_maximum_delay_to_return
    Returns:
        A_list_of_random_floats_between_0_and_max_delay
    """
    return await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns_a_random_float_between_0_and_max_delay
    Args:
        max_delay: The_maximum_delay_to_return
    Returns:
        A random_float_between_0_and_max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand


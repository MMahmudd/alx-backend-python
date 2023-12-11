#!/usr/bin/env python3
"""Has_a_coroutine_that_delays_a_certain_amount_of_time_and_returns_it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns_a_random_float_between_0_and_max_delay
    Args:
        max_delay: The_maximum_delay_to_return
    Returns:
        A random_float_between_0_and max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand

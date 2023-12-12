#!/usr/bin/env python3
"""Has a coroutine that delays a certain amount of time and returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns_a_random_float_between_0_and_max_delay
    Args:
        max_ddelay: The_maximum_delay_to_return
    Returns:
        A random_float_between_0_and_max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand

#!/usr/bin/env python3
"""Hold_a_method that_spawns_Tasks_times_with a
specified_delay_between_each_call."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns_wait random n_times with_a_specified_delay
    between_each_call.
    Args:
        n: number_of times_to_spawn wait random
        max_delay: maximum_delay_between_each_call
    Returns:
        list_of_delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

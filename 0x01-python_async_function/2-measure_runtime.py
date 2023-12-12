#!/usr/bin/env python3
"""Has_amethod_that_measure_the_total_execution_time_of
a function"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure_the_total_execution_time_of_a_function
    Args:
        n: the_number_of_coroutines_to_launch
        max_delay: the_maximum_amountof_timeto wait_for_each_coroutine
    Returns: elapsed time in seconds
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n

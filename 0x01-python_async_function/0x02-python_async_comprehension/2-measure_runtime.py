#!/usr/bin/env python3
"""A python_module_to_measure_the_execution_time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measureRuntime - function_execute_async_com 4_times
    Argument:
        no_hing
    Return:
        the_total_exection_time_required_to_complete_the_task
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)

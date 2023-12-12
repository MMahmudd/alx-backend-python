#!/usr/bin/env python3
""" _ python_module_to_loop_10_times """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    asyncGenerator - function_to_loop_10_times
    Argument:
        no_arguments
    Return_:
        no_thing
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

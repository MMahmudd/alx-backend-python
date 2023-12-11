#!/usr/bin/env python3
"""Holds_a_method_that_returns_a_task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns_a_task_that_waits_for_a_random_number_of_seconds
    """
    return asyncio.create_task(wait_random(max_delay))

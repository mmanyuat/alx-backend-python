#!/usr/bin/env python3
"""
Module to measure the runtime of the wait_n coroutine.
"""

import time
import asyncio
from typing import Callable

# Import wait_n using __import__
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n

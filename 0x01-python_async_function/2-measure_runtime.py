#!/usr/bin/env python3
"""
Module to measure the runtime of an asynchronous function.
"""

import time
import asyncio
from typing import Union
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total runtime for wait_n(n, max_delay).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n

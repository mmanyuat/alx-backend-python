#!/usr/bin/env python3
"""
Coroutine that generates random numbers between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously waits for 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

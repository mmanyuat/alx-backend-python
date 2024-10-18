#!/usr/bin/env python3
"""
Module that defines the asynchronous coroutine wait_random.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    for a random delay between 0 and max_delay seconds
    and eventually returns the delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

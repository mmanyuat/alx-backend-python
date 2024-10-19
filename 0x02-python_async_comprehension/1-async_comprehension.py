#!/usr/bin/env python3
"""
Coroutine 10 random numbers using async comprehension over async_generator.
"""

from typing import List
# Import async_generator using __import__
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 randons using an async comprehension over async_generator.
    """
    return [i async for i in async_generator()]

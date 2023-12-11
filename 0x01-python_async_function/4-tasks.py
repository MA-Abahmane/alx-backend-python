#!/usr/bin/env python3

"""
Take the code from wait_n and alter it into a new function task_wait_n
The code is nearly identical to wait_n except task_wait_random is being called
"""


import asyncio as asy
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """ an async routine that takes in 2 arg and returns a list of delays """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asy.gather(*tasks)
    return delays

#!/usr/bin/env python3
from random import randint
import asyncio

async def gen_foo(item):
    sleep_time_in_msec = randint(10,500)
    await asyncio.sleep(sleep_time_in_msec / 1000)
    print(f"{item}: Sleep time {sleep_time_in_msec} msec")
    return (sleep_time_in_msec, item)

async def run_async(x):
    res = asyncio.gather(*map(gen_foo, x))
    return await res

async def run_sync(x):
    return [await gen_foo(item) for item in x]


async def main():
    x = [1, 2, 3, 4]
    # res = await run_async(x)
    res = await run_sync(x)
    print(f"{res}")
    total_time = sum(map(lambda x: x[0], res))
    print(f"Total time {total_time}")




loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# asyncio.run(main())

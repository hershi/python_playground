#!/usr/bin/env python3
import sys
import asyncio
from random import randint

async def gen_foo(item):
    sleep_time_in_msec = 1000
    await asyncio.sleep(sleep_time_in_msec / 1000)
    print(f"{item}: Sleep time {sleep_time_in_msec} msec")
    return (sleep_time_in_msec, item)

async def run_async(x):
    res = asyncio.gather(*map(gen_foo, x))
    return await res

async def run_sync(x):
    return [await gen_foo(item) for item in x]


async def main():
    x = [1, 2, 3, 4, 5]

    if len (sys.argv) > 1 and sys.argv[1] == '--async':
        res = await run_async(x)
    else:
        res = await run_sync(x)

    print(f"{res}")
    total_time = sum(map(lambda x: x[0], res))
    print(f"Total time {total_time}")


asyncio.run(main())

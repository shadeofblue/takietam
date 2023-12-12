import asyncio
import functools
from typing import AsyncGenerator

async def make_awaitable(value):
    return value

async def make_awaitable_list(l):
    for i in l:
        yield i

async def countdown(cnt):
    for i in reversed(range(cnt)):
        await asyncio.sleep(0.5)
        yield i

async def process(input_gen: AsyncGenerator):
    async for i in input_gen:
        await asyncio.sleep(1)
        yield i

async def main():
    # async for i in countdown(10, functools.partial(asyncio.sleep, 1)):
    #     print("main", i)
    #
    # async for i in countdown(10, functools.partial(make_awaitable, 1)):
    #     print("main", i)

    async for i in process(make_awaitable_list([1, 2, 3])):
        print(i)

asyncio.run(main())



import asyncio
import random


async def number(delay: int = 1):
    await asyncio.sleep(delay)
    return delay


async def main():
    print("start")
    for t in asyncio.as_completed([asyncio.create_task(number(i)) for i in [random.randint(0, 10) for _ in range(10)]]):
        print(await t)

asyncio.run(main())

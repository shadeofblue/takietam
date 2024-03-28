import asyncio
import argparse
from typing import Coroutine

async def delay_task(coro: Coroutine, delay: float):
    try:
        await asyncio.sleep(delay)
    except asyncio.CancelledError:
        print("cancelled...")
        coro.close()
        raise
    else:
        return await coro

def create_delayed_task(coro: Coroutine, delay: float):
    return asyncio.create_task(delay_task(coro, delay))

async def echo(v):
    print(v)

async def main(len_: int, delay: float):
    t = create_delayed_task(echo("dupa"), delay)
    print(t)

    for i in range(len_):
        print(i)
        await asyncio.sleep(1)

    t.cancel()

parser = argparse.ArgumentParser()
parser.add_argument("len", type=int)
parser.add_argument("delay", type=float)
args = parser.parse_args()

asyncio.run(main(args.len, args.delay))
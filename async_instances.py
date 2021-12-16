import asyncio
import random


async def add(a: list):
    for i in range(10):
        s = random.randint(1, 7)
        print(f"will add something in {s}s.")
        await asyncio.sleep(s)
        a.append(".")


async def run_add(a: list):
    print("run_add start")
    await add(a)
    print("run_add end")


def add_instances():
    instances = []
    asyncio.create_task(run_add(instances))
    return instances


async def main():
    instances = add_instances()
    try:
        while True:
            print(instances)
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("cancelled")

asyncio.run(main())

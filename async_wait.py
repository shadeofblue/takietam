import asyncio


async def wait(duration):
    print(f"waiting {duration}s ...")
    await asyncio.sleep(duration)
    print(f"finished waiting {duration}s ...")
    return f"waited for: {duration}"

async def main():
    a = wait(1)
    b = asyncio.ensure_future(wait(2))
    c = asyncio.create_task(wait(3))

    sleep_duration = 5

    print(f"sleeping for {sleep_duration} s first...")
    await asyncio.sleep(sleep_duration)
    print(f"finished sleeping for {sleep_duration} s...")

    print("result of a: ", await a)
    print("result of b: ", await b)
    print("result of c: ", await c)

asyncio.run(main())



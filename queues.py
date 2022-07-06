import asyncio


async def counter(q):
    cnt = 0
    while True:
        q.put_nowait(cnt)
        cnt += 1
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            return


async def consumer(q):
    while True:
        try:
            print(await q.get())
        except asyncio.CancelledError:
            return


async def main():
    q = asyncio.Queue()  # must be instantiated while the asyncio loop is running
    tasks = [
        asyncio.create_task(counter(q)),
        asyncio.create_task(consumer(q)),
    ]

    print("starting the wait")
    for i in range(10):
        await asyncio.sleep(1)

    print("cancelling tasks")

    for t in tasks:
        t.cancel()

    print("?")
    await asyncio.gather(*tasks)
    print("...")

    await asyncio.sleep(5)
    print("done")



asyncio.run(main())

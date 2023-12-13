import asyncio


async def cwait(c: asyncio.Condition, m: str):
    async with c:
        await c.wait()
        print("waited: ", m)

async def counter(n: int):
    nstart = n
    for i in range(n):
        await asyncio.sleep(1)
        print("counter: ", nstart - i)

async def main():
    c = asyncio.Condition()

    for i in range(10):
        asyncio.create_task(cwait(c, str(i+1)))

    print("started condition wait tasks...")

    await counter(1)

    async with c:
        c.notify(5)

    print("notified 5 of them...")

    await counter(5)

    async with c:
        c.notify_all()

    print("notified the rest...")

    await counter(5)

asyncio.run(main())

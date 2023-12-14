import asyncio

some_counter = 0

async def cwait(c: asyncio.Condition, m: str):
    async with c:
        await c.wait()
        print("waited: ", m)

async def counter(n: int):
    nstart = n
    for i in range(n):
        await asyncio.sleep(1)
        print("counter: ", nstart - i)

async def inc_some_counter():
    global some_counter
    while True:
        some_counter += 1
        await asyncio.sleep(0.001)

async def wait_come_counter(c: asyncio.Condition, value):
    async with c:
        await c.wait_for(lambda: some_counter > value)
        print("finished waiting for:", value, " actual: ", some_counter)

async def main():
    c = asyncio.Condition()

    asyncio.create_task(inc_some_counter())

    asyncio.create_task(wait_come_counter(c, 100))
    asyncio.create_task(wait_come_counter(c, 1000))

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

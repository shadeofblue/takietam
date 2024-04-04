import asyncio
from contextlib import asynccontextmanager

async def error_after(n):
    for i in range(n):
        print(f"{i}/{n} ... ")
        await asyncio.sleep(1)

    raise Exception(f"blah {n}")


@asynccontextmanager
async def some_context():
    print("context started... ")
    errors_after = [3, 6, 9, 12, 15]
    tasks = [asyncio.create_task(error_after(n)) for n in errors_after]

    print("context initialization finished, tasks started...")

    yield

    print("context shutting down...")

    for t in tasks:
        t.cancel()

    print("tasks cancelled")

    results = await asyncio.gather(*tasks, return_exceptions=True)

    # try:
    #     results = await asyncio.gather(*tasks, return_exceptions=True)
    # except Exception as e:
    #     print("Error :", e)

    print("results: ", results)

    print("context shutdown")

async def run():
    async with some_context():
        print("main task started...")

        await asyncio.sleep(4)

        print("main task finished...")

asyncio.run(run())


import asyncio

q = asyncio.Queue()
e = None

class MyException(Exception):
    ...


async def fill_queue(delay):
    cnt = 1
    while True:
        await asyncio.sleep(delay)
        q.put_nowait(cnt)
        cnt += 1

async def counter():
    cnt = 1
    while True:
        await asyncio.sleep(1)
        print("counter: ", cnt)
        cnt += 1

async def consume_queue():
    return await q.get()

async def cancel_task(t: asyncio.Task, delay):
    await asyncio.sleep(delay)
    t.cancel()

async def raise_after(t: asyncio.Task, delay):
    global e
    await asyncio.sleep(delay)
    try:
        raise MyException("my exception")
    except Exception as my_e:
        e = my_e
        t.cancel()


async def get_queue_val(raise_delay):
    cq_task = asyncio.create_task(consume_queue())
    asyncio.create_task(raise_after(cq_task, raise_delay))

    try:
        await cq_task
        return cq_task.result()
    except asyncio.CancelledError:
        if e:
            raise e
        return None

async def main():
    asyncio.create_task(fill_queue(5))
    asyncio.create_task(counter())
    print("queue result: ", await get_queue_val(4))

asyncio.run(main())
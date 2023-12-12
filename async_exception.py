import asyncio

async def task(max_cnt, raise_after = None):
    cnt = 0
    while cnt < max_cnt:
        cnt += 1
        print(f"{cnt} ...")
        await asyncio.sleep(1)

        if raise_after and cnt > raise_after:
            raise Exception(cnt)

    return "YAY!"

async def main():
    tsk = asyncio.create_task(task(4))

    print("main start sleep...")

    await asyncio.sleep(5)

    print("main end sleep...")

    tsk.cancel()

    print("main cancelled...")

    try:
        await asyncio.gather(tsk)
        print("result ------------------------ ", tsk.result())
    except asyncio.CancelledError:
        print("cancelled okay")

    print("main end...")

asyncio.run(main())

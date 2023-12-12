import asyncio
async def test():
    cnt = 1
    while True:
        print(f"{cnt} ...")
        await asyncio.sleep(1)
        cnt += 1

async def main():
    tsk = asyncio.create_task(test())

    print("main start sleep...")

    await asyncio.sleep(10)

    print("main end sleep...")

    tsk.cancel()

    print("main cancelled...")

    try:
        await asyncio.gather(tsk)
    except asyncio.CancelledError:
        print("cancelled okay")

    print("main end...")

asyncio.run(main())

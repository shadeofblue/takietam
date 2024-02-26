import asyncio

async def sleep(delay):
    try:
        await asyncio.sleep(delay)
    except asyncio.CancelledError:
        print("sleep Cancelled?")
        raise
    except KeyboardInterrupt:
        print("sleep CtrlC!")
        raise


async def test_sleep(n):
    for i in range(n):
        print(i)
        try:
            await sleep(1)
        except asyncio.CancelledError:
            print("test sleep Cancelled?")
            raise
        except KeyboardInterrupt:
            print("test sleep CtrlC!")
            raise


async def run():
    t = asyncio.create_task(test_sleep(10))

    try:
        await t
    except asyncio.CancelledError:
        print("run Cancelled?")
        raise
    except KeyboardInterrupt:
        print("run CtrlC!")
        raise

    print("run over")
    await t

# try:
#     asyncio.run(run())
# except KeyboardInterrupt:
#     print("main CtrlC...")
# print("?")

loop = asyncio.get_event_loop()
task = loop.create_task(run())

try:
    loop.run_until_complete(task)
except KeyboardInterrupt:
    print("main CtrlC...")
    task.cancel()

    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt:
        print("main CtrlC again...")
    except asyncio.CancelledError:
        print("main Cancelled...")

print("?")
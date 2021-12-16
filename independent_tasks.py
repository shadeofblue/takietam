import asyncio
import time


async def say_after(delay, what):
    for i in range(delay):
        await asyncio.sleep(1)
        print(f"...{delay-i}: {what}")
    print(f"!!! {what} !!!")


async def main():
    task1 = asyncio.create_task(
        say_after(5, 'hello'))

    task2 = asyncio.create_task(
        say_after(10, 'world'))

    print(f"started at {time.strftime('%X')}")

    for i in range(3):
        print(".")
        await asyncio.sleep(1)

    await task1

    print("past task 1")

    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
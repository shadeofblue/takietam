import asyncio
import aiostream


async def numbers(count: int, delay: int = 1, id=""):
    for i in range(count):
        await asyncio.sleep(delay)
        yield i+1, id


async def main():
    print("start")

    nums1 = numbers(10, 3, "1: ")
    nums2 = numbers(5, 10, "2: ")

    async with aiostream.stream.merge(nums1, nums2).stream() as s:
        async for n, id in s:
            print(f"{id}{n}")

    print("stop")


asyncio.run(main())

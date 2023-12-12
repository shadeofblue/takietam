import asyncio

async def test1():
    return "foo"

async def test2():
    raise RuntimeError("bar")

async def main():
    t1 = asyncio.create_task(test1())
    t2 = asyncio.create_task(test2())

    print(await t1)
    print(await t2)

asyncio.run(main())
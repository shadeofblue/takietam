import asyncio
import aiofiles
import functools
import sys

FILE_READ_INTERVAL = 1.0


async def get_pipe_reader(stream):
    loop = asyncio.get_event_loop()
    reader = asyncio.StreamReader(loop=loop)
    await loop.connect_read_pipe(functools.partial(asyncio.StreamReaderProtocol, reader), stream)
    return reader


async def main():

    async def echo_stdin():
        stdin_reader = await get_pipe_reader(sys.stdin)
        while True:
            print((await stdin_reader.readline()).decode("utf-8"))

    async def counter():
        c = 0
        while True:
            c += 1
            print(c)
            await asyncio.sleep(1)

    async def echo_file():
        async with aiofiles.open("somefile.txt", "w+b") as f:
            while True:
                line = await f.readline()
                if line:
                    print(line.decode("utf-8"))
                else:
                    await asyncio.sleep(FILE_READ_INTERVAL)

    await asyncio.gather(
        asyncio.create_task(counter()),
        asyncio.create_task(echo_stdin()),
        asyncio.create_task(echo_file()),
    )


asyncio.run(main())

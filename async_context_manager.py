import asyncio
from typing import AsyncContextManager, Optional
from contextlib import AsyncExitStack


class Engine(AsyncContextManager):
    def __init__(self):
        print(f"{self.__class__} init")
        self._stack = AsyncExitStack()

    async def __aenter__(self) -> "Engine":
        print(f"{self.__class__} enter async context")
        return self

    async def __aexit__(self, *exc_info):
        print(f"{self.__class__} exit async context {exc_info}")
        await self._stack.aclose()

    async def execute_task(self, count: int):
        async with Executor(self) as executor:
            async for i in executor.submit(count):
                yield i


class Executor(AsyncContextManager):
    def __init__(self, _engine: Optional[Engine] = None):
        print(f"{self.__class__} init")
        self._stack = AsyncExitStack()
        self.__standalone = False

        if not _engine:
            self._engine = Engine()
            self.__standalone = True

    async def __aenter__(self) -> "Executor":
        if self.__standalone:
            await self._stack.enter_async_context(self._engine)

        print(f"{self.__class__} enter async context")
        return self

    async def __aexit__(self, *exc_info):
        print(f"{self.__class__} exit async context {exc_info}")
        await self._stack.aclose()

    async def submit(self, count: int):
        print(f"{self.__class__} submit")
        for i in range(count):
            yield i+1


async def main():
    print("------------ before -------------")

    async with Executor() as one:
        async for i in one.submit(5):
            print(i)

    print("------------ after -------------")

    async with Engine() as engine:
        async for i in engine.execute_task(5):
            print(i)

asyncio.run(main())



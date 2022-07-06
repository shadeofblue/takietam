import asyncio
from contextlib import asynccontextmanager
from typing import AsyncContextManager


class ACM(AsyncContextManager):
    __already_entered = False

    def __init__(self):
        print(f"{self} init")

    def __repr__(self):
        return f"{self.__class__.__name__}"

    async def __aenter__(self) -> "ACM":
        if self.__already_entered:
            return self

        self.__already_entered = True
        print(f"{self} enter async context")
        return self

    async def __aexit__(self, *exc_info):
        print(f"{self} exit async context {exc_info}")
        return True

    async def close(self):
        await self.__aexit__()


class Foo(ACM):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def __repr__(self):
        return f"{super().__repr__()}: {self.name}"


class Bar:

    @staticmethod
    async def create_foo(name):
        foo = Foo(name)
        await foo.__aenter__()
        return foo

    @staticmethod
    def foo(name):
        return Foo(name)


async def main():
    bar = Bar()

    async with await bar.create_foo(1) as foo:
        print(foo)
        raise Exception()

    print("----------------")

    async with bar.foo(2) as foo:
        print(foo)
        raise Exception()

    print("----------------")

    foo = await bar.create_foo(3)
    print(foo)
    await foo.close()

asyncio.run(main())



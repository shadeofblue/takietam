import abc
import asyncio


class Base:
    def a(self):
        print("a")

    async def b(self):
        await asyncio.sleep(0.01)
        print("b")


class Wrapping(abc.ABC):
    def __init__(self, base: Base):
        self.base = base

    def __getattr__(self, item):
        return getattr(self.base, item)


class Foo(Wrapping):
    pass


class Bar(Wrapping):
    def a(self):
        print("aaa")

    async def b(self):
        await asyncio.sleep(0.01)
        print("bbb")


async def main():
    foo = Foo(Base())
    bar = Bar(Base())

    foo.a()
    await foo.b()

    bar.a()
    await bar.b()


asyncio.run(main())

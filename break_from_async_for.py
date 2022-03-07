import asyncio
import itertools
from typing import AsyncGenerator, AsyncIterator


async def numbers(delay: int = 1):
    g = itertools.count()
    generator_exit = False

    for i in g:
        await asyncio.sleep(delay)
        print("before", i)
        try:
            yield i
        except GeneratorExit:
            print("---------------------------------- GENERATOR EXIT")
            import traceback
            traceback.print_stack()
            generator_exit = True
        except:
            print("---------------------------------- GENRATOR THROW")
            raise

        print("after", i)

        if generator_exit:
            break


class ClassGen(AsyncIterator):
    def __init__(self):
        self.done = False
        self.g = itertools.count()

    async def asend(self, __value):
        return await super().asend(__value)

    async def athrow(self, __typ, __val = None, __tb = None):
        self.done = True
        return await super().athrow(__typ, __val, __tb)

    async def aclose(self):
        self.done = True

    async def __anext__(self):
        if self.done:
            raise StopAsyncIteration()
        return self.g.__next__()


async def worker(gen, cutoff=None):
    cnt = 0
    async for i in gen:
        yield i
        if cnt >= cutoff:
            # no, it just drops the generator and the code
            # never has a chance to return to the generator
            # break

            # the generator correctly receives the exception as long as the code calling this
            # worker passes the exception to the generator
            raise Exception("a")

            # this correctly bubbles upwards
            await gen.aclose()
        cnt += 1


async def main(cutoff):
    print("start")

    nums = numbers()
    try:
        async for w in worker(nums, cutoff):
            print(w)
    except Exception as e:
        print("----------------------------------------------------------------------", e)
        await nums.athrow(e)

    print("stop")

try:
    asyncio.run(main(1))
except:
    pass
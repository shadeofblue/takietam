import asyncio
import itertools


async def numbers(delay: int = 1):
    g = itertools.count()
    generator_exit = False

    for i in g:
        await asyncio.sleep(delay)
        print("before", i)
        try:
            yield i
        except GeneratorExit:
            generator_exit = True

        print("after", i)

        if generator_exit:
            break


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
            # raise Exception("a")

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
        await nums.athrow(e)

    print("stop")


asyncio.run(main(1))

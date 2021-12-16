import asyncio

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0


async def handler1():
    global cnt1
    print(f"handler1a {cnt1}")
    future_result = yield cnt1, True
    result = await future_result
    print(f"handler1a got {result}")
    cnt1 += 1

    print(f"handler1b {cnt1}")
    future_result = yield cnt1, True
    result = await future_result
    print(f"handler1b got {result}")
    cnt1 += 1



async def handler2():
    global cnt2
    print(f"handler2 {cnt2}")
    yield cnt2, False
    cnt2 += 1



async def handler3():
    global cnt3
    for i in range(3):
        print(f"handler3 {cnt3}")
        future_result = yield cnt3, False
        result = await future_result
        print(f"handler3 got {result}")
        cnt3 += 1


async def handler4():
    global cnt4
    for i in range(3):
        print(f"handler4 {cnt4}")
        yield cnt4, False
        cnt4 += 1



async def get_results(cnt):
    await asyncio.sleep(1)
    result = f"result {cnt}"
    print(result)
    return result


async def consumer():
    handlers = [handler1, handler2, handler3, handler4]
    for handler in handlers:
        print(f"-------- handler loop {handler}")
        gen = handler()

        h, blocking = await gen.__anext__()
        while h is not None:
            await asyncio.sleep(0.1)
            print(f"handler {handler}, h {h}, blocking {blocking}")
            l = asyncio.get_event_loop()
            try:
                if blocking:
                    r = await get_results(h)
                    fr = l.create_future()
                    fr.set_result(r)
                    h, blocking = await gen.asend(fr)
                else:
                    r = asyncio.create_task(get_results(h))
                    h, blocking = await gen.asend(r)
            except StopAsyncIteration:
                print(f"handler {handler} SAI")
                break

asyncio.run(consumer())
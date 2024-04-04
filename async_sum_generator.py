import asyncio
async def identity_async(v):
    return v

def identity(v):
    return v

async def get_sum_async():
    # print(sum((await identity_async(i) for i in range(10))))  # TypeError: 'async_generator' object is not iterable
    print(sum([await identity_async(i) for i in range(10)]))

def get_sum():
    print(sum(identity(i) for i in range(10)))

get_sum()
print(sum(range(10)))
asyncio.run(get_sum_async())

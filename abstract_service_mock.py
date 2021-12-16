import asyncio
from dataclasses import dataclass
import enum
import random
from typing import Optional, Any


class WorkContext:
    def __init__(self):
        self._steps = []

    def run(self, step):
        self._steps.append(step)

    def commit(self):
        steps = self._steps
        self._steps = []
        return steps


class SignalType(enum.Enum):
    shutdown = "shutdown"
    generic = "generic"


@dataclass
class ControlSignal:
    message: Optional[Any] = None
    signal_type: SignalType = SignalType.generic

    @property
    def is_shutdown(self):
        return self.signal_type == SignalType.shutdown


@dataclass
class StatusSignal:
    message: Any
    response_to: Optional[ControlSignal] = None


class Service:
    def __init__(self, ctx: WorkContext):
        self.ctx = ctx
        self.__inqueue: asyncio.Queue[ControlSignal] = asyncio.Queue()
        self.__outqueue: asyncio.Queue[StatusSignal] = asyncio.Queue()
        self.state = None

    async def send(self, message: Optional[Any] = None, signal_type: SignalType = SignalType.generic):
        await self.__inqueue.put(ControlSignal(message=message, signal_type=signal_type))

    def send_nowait(self, message: Optional[Any] = None, signal_type: SignalType = SignalType.generic):
        self.__inqueue.put_nowait(ControlSignal(message=message, signal_type=signal_type))

    def send_shutdown(self):
        self.send_nowait(signal_type=SignalType.shutdown)

    async def receive(self) -> StatusSignal:
        return await self.__outqueue.get()

    def receive_nowait(self) -> Optional[StatusSignal]:
        try:
            return self.__outqueue.get_nowait()
        except asyncio.QueueEmpty:
            pass

    async def __respond(self, message: Optional[Any], response_to: Optional[ControlSignal] = None):
        await self.__outqueue.put(StatusSignal(message=message, response_to=response_to))

    def __respond_nowait(self, message: Optional[Any], response_to: Optional[ControlSignal] = None):
        self.__outqueue.put_nowait(StatusSignal(message=message, response_to=response_to))

    async def run(self):

        while True:
            i = await self.__inqueue.get()

            if i.is_shutdown:
                await self.__respond(f"I'm shutting down", i)
                break
            else:
                await self.__respond(f"received {i.message}", i)
                self.ctx.run(f"do something with {i.message}")
                await result

                self.ctx.run(f"do something else with {i.message}")
                yield self.ctx.commit()



async def get_input():
    while True:
        n = random.randint(1, 5)
        yield n
        await asyncio.sleep(n)


def get_input_queue():
    iq = asyncio.Queue()

    async def input_to_queue():
        async for i in get_input():
            await iq.put(i)

    asyncio.create_task(input_to_queue())

    return iq


async def input_handler(s: Service):
    iq = get_input_queue()
    cnt = 3000
    while cnt > 0:
        try:
            v = iq.get_nowait()
            print(f"sending input to service: {v}")
            s.send_nowait(v)
        except asyncio.QueueEmpty:
            pass

        await asyncio.sleep(0.01)
        cnt -= 1

    print("time's up")
    s.send_shutdown()


class Executor:
    async def _run_batch(self, batch):
        return f"exescript sent {batch}"

    async def _run_batches(self, s: Service):
        batches = s.run()
        async for batch in batches:
            result = self._run_batch(batch)
            await batches.asend(result)

        s.state = "shutdown"

    async def run_service(self) -> Service:
        ctx = WorkContext()
        s = Service(ctx)
        s.state = "running"

        asyncio.create_task(self._run_batches(s))

        return s


async def main():

    service = await Executor().run_service()

    asyncio.create_task(input_handler(service))

    while service.state == "running":
        o = await service.receive()
        print(f"input {o.response_to} -> service says: '{o.message}'")

asyncio.run(main())
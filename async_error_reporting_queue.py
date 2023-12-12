import asyncio
import dataclasses
from typing import Generic, Optional, TypeVar

QueueItem = TypeVar("QueueItem")

class ErrorReportingQueue(asyncio.Queue, Generic[QueueItem]):
    __error: Optional[BaseException]
    __error_event: asyncio.Event

    def __init__(self, *args, **kwargs):
        self.__error = None
        self.__error_event = asyncio.Event()
        super().__init__(*args, **kwargs)

    def get_nowait(self) -> QueueItem:
        if self.empty() and self.__error:
            raise self.__error
        return super().get_nowait()

    async def get(self) -> QueueItem:
        get_task = asyncio.create_task(super().get())
        event_task = asyncio.create_task(self.__error_event.wait())
        completed, _ = await asyncio.wait(
            [event_task, get_task],
            return_when=asyncio.FIRST_COMPLETED
        )
        if event_task in completed:
            raise self.__error

        return get_task.result()

    def set_exception(self, exc: BaseException):
        self.__error = exc
        self.__error_event.set()

    async def put(self, item: QueueItem):
        await super().put(item)

    def put_nowait(self, item: QueueItem):
        super().put_nowait(item)


@dataclasses.dataclass
class Container:
    value: str

q: ErrorReportingQueue[Container] = ErrorReportingQueue()

async def queue_values():
    await asyncio.sleep(1)
    q.put_nowait(Container("1"))
    await asyncio.sleep(1)
    q.put_nowait(Container("2"))
    await asyncio.sleep(1)
    q.set_exception(RuntimeError("test"))

async def main():
    t = asyncio.create_task(queue_values())
    while True:
        try:
            v = q.get_nowait()
            print(v.value)
        except asyncio.QueueEmpty:
            await asyncio.sleep(0.01)


asyncio.run(main())

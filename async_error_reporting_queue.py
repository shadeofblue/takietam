import asyncio
import dataclasses
from typing import Generic, Optional, TypeVar

QueueItem = TypeVar("QueueItem")

class ErrorReportingQueue(asyncio.Queue, Generic[QueueItem]):
    _error: Optional[BaseException]
    _error_event: asyncio.Event

    def __init__(self, *args, **kwargs):
        self._error = None
        self._error_event = asyncio.Event()
        super().__init__(*args, **kwargs)

    def get_nowait(self) -> QueueItem:
        if self.empty() and self._error:
            raise self._error
        return super().get_nowait()

    async def get(self) -> QueueItem:
        error_task = asyncio.create_task(self._error_event.wait())
        get_task = asyncio.create_task(super().get())
        done, _ = await asyncio.wait(
            [error_task, get_task],
            return_when=asyncio.FIRST_COMPLETED
        )

        if get_task in done:
            return await get_task

        raise self._error

    async def put(self, item: QueueItem):
        await super().put(item)

    def put_nowait(self, item: QueueItem):
        super().put_nowait(item)

    def set_exception(self, exc: BaseException):
        self._error = exc
        self._error_event.set()

    def reset_exception(self):
        self._error = None
        self._error_event.clear()


@dataclasses.dataclass
class Container:
    value: str


async def queue_values(q: ErrorReportingQueue):
    await asyncio.sleep(1)
    q.put_nowait(Container("1"))
    await asyncio.sleep(1)
    q.put_nowait(Container("2"))
    await asyncio.sleep(1)
    q.put_nowait(Container("3"))
    q.set_exception(RuntimeError("test"))
    await asyncio.sleep(1)
    q.put_nowait(Container("4"))

async def test_get():
    q: ErrorReportingQueue[Container] = ErrorReportingQueue()
    asyncio.create_task(queue_values(q))
    while True:
        v = await q.get()
        print(v.value)

async def test_get_nowait():
    q: ErrorReportingQueue[Container] = ErrorReportingQueue()
    asyncio.create_task(queue_values(q))
    while True:
        try:
            v = q.get_nowait()
            print(v.value)
        except asyncio.QueueEmpty:
            await asyncio.sleep(0.01)

async def main():
    await test_get_nowait()



asyncio.run(main())

import aiohttp
import asyncio

ADDRESS="ws://127.0.0.1:1111/"

REQUEST_DATA = b"test message"
TIMEOUT = 60.0


async def test():
    ws_session = aiohttp.ClientSession()
    running = True
    multiplier = 1
    while running:
        try:
            async with ws_session.ws_connect(
                    ADDRESS,
            ) as ws:

                data = REQUEST_DATA * multiplier
                print("------------------- SENDING ------------------- ", len(data), " bytes")
                await ws.send_bytes(data + b" " + str(len(data)).encode("ascii"))

                ws_response = await ws.receive(TIMEOUT)

                print("------------------- RESPONSE -------------------")
                print(ws_response.data)
                print("------------------------------------------------")

                multiplier *= 2

        except asyncio.CancelledError:
            running = False

    await ws_session.close()

try:
    asyncio.run(test())
except KeyboardInterrupt:
    pass

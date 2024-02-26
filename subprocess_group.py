import argparse
import asyncio
import os


async def main(spawn_child=False):
    print(f"{os.getpid()=}, {os.getgid()=}, {os.getpgrp()=}")

    if spawn_child:
        print("spawning a child")
        process = await asyncio.create_subprocess_exec(
            "python", __file__,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            # preexec_fn=os.setpgrp,
            start_new_session=True,
        )

        stdout, stderr = await process.communicate()

        print(f"   {stdout.decode('utf-8')}")

    await asyncio.sleep(60)

parser = argparse.ArgumentParser()
parser.add_argument("--spawn-child", action="store_true")
args = parser.parse_args()

asyncio.run(main(args.spawn_child))
import argparse
import tempfile
import time

_, path = tempfile.mkstemp(prefix="takietam-subprocess-child-")

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sleep-count", type=int, default=100)
parser.add_argument("-e", "--error-on", type=int)
args = parser.parse_args()

sleep_cnt = args.sleep_count

while sleep_cnt > 0:

    with open(path, "a") as f:
        f.write(f"{sleep_cnt}\n")

    print(sleep_cnt)

    if args.error_on and args.error_on >= sleep_cnt:
        raise Exception("erroring out as instructed ...")

    sleep_cnt -= 1
    time.sleep(1)

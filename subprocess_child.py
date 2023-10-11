import argparse
import tempfile
import time
import sys
import logging

logging.basicConfig(filename='subprocess.log', level=logging.DEBUG)

logger = logging.getLogger(__name__)

_, path = tempfile.mkstemp(prefix="takietam-subprocess-child-")

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sleep-count", type=int, default=100)
parser.add_argument("-e", "--error-on", type=int)
args = parser.parse_args()

sleep_cnt = args.sleep_count

try:
    while sleep_cnt > 0:

        with open(path, "a") as f:
            f.write(f"{sleep_cnt}\n")

        logger.info(sleep_cnt)
        print(sleep_cnt)
        sys.stdout.flush()

        if args.error_on and args.error_on >= sleep_cnt:
            raise Exception("erroring out as instructed ...")

        sleep_cnt -= 1
        time.sleep(1)
except Exception as e:
    logger.error(e)
    raise

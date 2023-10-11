import argparse
import subprocess
import time

OUTFILE = "subprocess.out"
ERRFILE = "subprocess.err"

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sleep-count", type=int, default=100)
parser.add_argument("-l", "--launch-count", type=int, default=10)
parser.add_argument("-e", "--error-on", type=int)
parser.add_argument("-n", "--new-session", action="store_true")
args = parser.parse_args()

cmd = [
    "python",
    "subprocess_child.py",
    "-s", str(args.sleep_count),
]

if args.error_on:
    cmd += ["-e", str(args.error_on)]

print(f"Launching: {cmd}, new_session={bool(args.new_session)}")

proc = subprocess.Popen(
    cmd,
    stdout=open(OUTFILE, "w") ,
    stderr=open(ERRFILE, "w"),
    start_new_session=bool(args.new_session),
)

launch_count = args.launch_count

while launch_count > 0:
    try:
        proc.communicate(timeout=1)
        print(
            f"exited {launch_count}\n"
            f"-- out --\n{open(OUTFILE, 'r').read()}\n-- err --\n{open(ERRFILE, 'r').read()}"
        )
        break
    except subprocess.TimeoutExpired:
        pass

    print(f"{launch_count}...")
    launch_count -= 1

launched = True

try:
    proc.communicate(timeout=1)
    launched = False
except:
    pass

print(f"finished waiting... launched: {launched}")

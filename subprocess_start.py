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

with open(OUTFILE, "w") as outfile, open(ERRFILE, "w") as errfile:
    proc = subprocess.Popen(
        cmd,
        stdout=outfile,
        stderr=errfile,
        start_new_session=bool(args.new_session),
    )

launch_count = args.launch_count

while launch_count > 0:
    try:
        out, err = proc.communicate(timeout=1)
        with open(OUTFILE, "r") as outfile, open(ERRFILE, "r") as errfile:
            print(
                f"exited {launch_count}\n"
                f"-- out --\n{outfile.read()}\n-- err --\n{errfile.read()}"
                f"-- out --\n{str(out)}\n-- err --\n{str(err)}"
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

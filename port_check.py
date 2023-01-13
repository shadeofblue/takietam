import socket
import subprocess
import sys


def get_free_port(range_start: int = 8080, range_end: int = 9090) -> int:
    for port in range(range_start, range_end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))

                if len(sys.argv) > 1:
                    print(sys.argv[1])
                    print(subprocess.run(["python", "port_check.py"] + sys.argv[2:],
                                         capture_output=True).stdout.decode("ascii"))

                #s.bind(("", port))
                return port
            except OSError:
                pass



print(get_free_port(), get_free_port(), get_free_port())


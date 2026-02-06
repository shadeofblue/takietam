import uuid
from base64 import urlsafe_b64encode

used = set()

LEN = 7

def gen_short_url():
    while True:
        candidate = urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8").strip("=")[:LEN]
        if candidate not in used:
            used.add(candidate)
            return candidate
        print("!!!!!!!!!!!!!!!!!!!!!!!", candidate)


for _ in range(1_000_000):
    gen_short_url()

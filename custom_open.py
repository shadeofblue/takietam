from contextlib import contextmanager


@contextmanager
def my_open(name, mode):
    try:
        f = open(name, mode)
        yield f
    except Exception:
        print("exception!")
        raise
    finally:
        print("close")
        f.close()


print("start")

with my_open("tttt", "w") as f:
    print("writing")
    f.write("aaaaa")
    print("written")
    raise Exception("asss")

print("end")

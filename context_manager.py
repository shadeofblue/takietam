from contextlib import contextmanager

@contextmanager
def cm1():
    print("cm1 start")
    try:
        yield
    finally:
        print("cm1 stop")

@contextmanager
def cm2():
    print("cm2 start")
    try:
        with cm1():
            print("cm2 ...")
            yield
    finally:
        print("cm2 end")

@contextmanager
def cm3():
    print("cm3 start")
    with cm1():
        print("cm3 ...")
        yield
    print("cm3 end")

with cm3():
    print("doing something...")
    # raise Exception("sss")

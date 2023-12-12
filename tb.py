import traceback
import sys

def inner():
    raise ValueError("test")

def middle():
    try:
        inner()
    except Exception:
        raise

def outer():

    class CustomException(Exception):
        ...

    try:
        middle()
    except Exception as e:
        raise CustomException() from e


def exception_causes(e: BaseException):
    causes = [f"{type(e)}: {e}"]
    if e.__cause__:
        causes.extend(exception_causes(e.__cause__))
    return causes

try:
    outer()
except Exception as e:
    print(exception_causes(e))

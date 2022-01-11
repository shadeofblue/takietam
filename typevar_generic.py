from typing import TypeVar, Type, Generic, List


class Base:
    pass


class A(Base):

    def __init__(self, a):
        self.a = a


class B(Base):
    def __init__(self, b):
        self.b = b


class C:
    def __init__(self, c):
        self.c = c


S = TypeVar("S", bound=Base)


def instantiate(cls: Type[S], *args, **kwargs) -> S:
    return cls(*args, **kwargs)


# valid, type checkers know that a is of type A
a = instantiate(A, 1)
print(a.a)

# valid, type checkers know that b is of type B
b = instantiate(B, 2)
print(b.b)

# type-invalid, but type checkers still know that c is of type C
c = instantiate(C, 3)
print(c.c)


class Factory(Generic[S]):

    @staticmethod
    def instantiate(cls: Type[S], *args, **kwargs) -> S:
        return cls(*args, **kwargs)


f: Factory[A] = Factory()

# valid
ia = f.instantiate(A, "F1")
print(ia.a)

# type-invalid, the factory is expected to be used only with A
ib = f.instantiate(B, "F2")  # type: ignore
print(ib.b)  # type: ignore

# valid factory
g: Factory[B] = Factory()

# type-invalid factory, since we only allow Factories to accept anything based on Base
h: Factory[C] = Factory()


T = TypeVar("T", str, int)


def add(a: T, b: T) -> T:
    return a+b


print(add(1, 2))


print(add("a", "b"))


# type-invalid (and won't run, but that's not the point)
# print(add(1, "a"))

def append_and_print_sum(l: List[T], a: T):
    l.append(a)
    s = l.pop(0)
    while len(l):
        s += l.pop(0)

    print(s)


# valid
append_and_print_sum([1, 2, 3], 4)

# valid
append_and_print_sum(["a", "b", "c"], "d")


# type-invalid (and won't run...)
# append_and_print_sum(["a", "b", "c"], 7)


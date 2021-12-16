a = [1,2,3]


def prepend(a):
    a = [0] + a
    print(f"inside {a}")


print(f"before {a}")
prepend(a)
print(f"after {a}")


print(a[-1])
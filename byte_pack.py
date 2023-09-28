v = b""


for i in range(32, 127):
    v += b"%c" % i


print(v)
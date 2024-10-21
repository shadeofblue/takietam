def test(v = list()):
    for i in v:
        print(i)
    v.append(1)

def test2(v = list()):
    for i in v:
        print(i)

def test3(v = ()):
    for i in v:
        print(i)


test()
test()
test()

test2()
test2((1, ))
test2((2, 3))

test3()
test3((1, ))
test3((2, 3))


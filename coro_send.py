async def test():
    print("dupa")

c = test()
print("created", c)
c.send(None)
print("executed", c)
c.close()
print("closed", c)

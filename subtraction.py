
def diff(a: str, b: str) -> str:
    sign = False

    if len(b) > len(a) or (len(b) == len(a) and b[0] > a[0]):
        a, b = b, a
        sign = True

    al = list(a)
    bl = list(b)
    carry = 0
    out = ""
    for i in range(max(len(a), len(b))):
        ad = al.pop() if len(al) else "0"
        bd = bl.pop() if len(bl) else "0"
        d = int(ad) - int(bd) + carry
        if d < 0:
            carry = -1
            d += 10
        out = str(d) + out

    out = out.lstrip("0")
    if sign:
        out = "-" + out

    print(a, "-", b, "=", out)

    return out


assert diff("300", "77") == "223"
assert diff("177", "23") == "154"
assert diff("10", "7") == "3"
assert diff("3", "7") == "-4"
assert diff("10", "113") == "-103"

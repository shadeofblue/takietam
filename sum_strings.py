
def sum_str(v1: str, v2: str):
    v1r = list(reversed(v1))
    v2r = list(reversed(v2))
    l = max(len(v1), len(v2))

    res = ""
    carry = 0
    zero = ord("0")

    for i in range(l):
        a = ord(v1r[i] if i < len(v1) else "0") - zero
        b = ord(v2r[i] if i < len(v2) else "0") - zero
        carry, current = divmod(a + b + carry, 10)
        res = chr(current + zero) + res

    if carry:
        res = chr(carry + zero) + res

    return res


def test_sum(v1: str, v2: str, expected: str):
    s = sum_str(v1, v2)
    print(f"{v1} + {v2} = {s}")
    try:
        assert s == expected, f"{s} != {expected}"
    except AssertionError as e:
        print("WRONG!!! ", str(e))


test_sum("1", "2", "3")
test_sum("111", "222", "333")
test_sum("103", "9", "112")
test_sum("666", "777", "1443")
test_sum("9999", "9999", "19998")
test_sum("0", "0", "0")


# 202

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            digits = []
            while n > 0:
                n, digit = divmod(n, 10)
                digits.append(digit)
                # print(f"{n=}, {digit=}")
            n = sum([n*n for n in digits])
            # print("--- ", digits, n)
        return False

n = 19
print(n)
print(Solution().isHappy(n))

n = 2
print(n)
print(Solution().isHappy(n))


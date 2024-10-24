# 12

class Solution:

    lookup = {
        0: ["I", "V"],
        1: ["X", "L"],
        2: ["C", "D"],
        3: ["M"]
    }

    def intToRoman(self, num: int) -> str:
        v = ""
        m = 0
        while num > 0:
            num, dd = divmod(num, 10)
            # print(f"{m=}, {num=}, {dd=}, {v=}")
            if dd == 0:
                pass
            elif dd < 4:
                v = self.lookup[m][0]*dd + v
            elif dd == 4:
                v = self.lookup[m][0] + self.lookup[m][1] + v
            elif dd < 9:
                v = self.lookup[m][1] + self.lookup[m][0]*(dd-5) + v
            else:
                v = self.lookup[m][0] + self.lookup[m + 1][0] + v
            m += 1

        return v


num = 3749
print(num)
print(Solution().intToRoman(num))

num = 58
print(num)
print(Solution().intToRoman(num))

num = 1994
print(num)
print(Solution().intToRoman(num))

num = 10
print(num)
print(Solution().intToRoman(num))

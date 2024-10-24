# 6

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]
        r = 0
        zig = True
        for c in s:
            rows[r] += c
            if zig:
                r += 1
            else:
                r -= 1
            if r >= numRows:
                r = numRows - 2
                zig = False
            elif r < 0:
                r = 1
                zig = True

            r = max(0, min(r, numRows - 1))

        return "".join(rows)


s = "PAYPALISHIRING"
print(s)
print(Solution().convert(s, 3))

print(s)
print(Solution().convert(s, 4))

s = "A"
print(s)
print(Solution().convert(s, 1))

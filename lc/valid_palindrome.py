# 125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = 0
        ri = len(s) - 1
        while li <= ri:
            lc = s[li].upper()
            rc = s[ri].upper()

            if not lc.isalnum():
                li += 1
                continue
            if not rc.isalnum():
                ri -= 1
                continue

            if lc != rc:
                return False

            li += 1
            ri -= 1

        return True

s = "A man, a plan, a canal: Panama"
print(s)
print(Solution().isPalindrome(s))

s = "race a car"
print(s)
print(Solution().isPalindrome(s))

s = " "
print(s)
print(Solution().isPalindrome(s))

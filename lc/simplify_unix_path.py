# 71
import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        input_elements = filter(None, re.split("/+", path))
        output_elements = []
        for e in input_elements:
            if e == ".":
                continue
            if e == "..":
                try:
                    output_elements.pop()
                except IndexError:
                    pass
                continue
            output_elements.append(e)
        return "/" + "/".join(output_elements)


s = Solution()
path = "/home/"
print(path)
print(s.simplifyPath(path))

path = "/home//foo/"
print(path)
print(s.simplifyPath(path))

path = "/home/user/Documents/../Pictures"
print(path)
print(s.simplifyPath(path))

path = "/../"
print(path)
print(s.simplifyPath(path))

path = "/.../a/../b/c/../d/./"
print(path)
print(s.simplifyPath(path))


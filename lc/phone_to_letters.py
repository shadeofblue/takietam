# 17
from typing import Dict, List

class Solution:
    def __init__(self):
        self.num_map: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:

        def translate(combination: str, digits: str):
            if not digits:
                if combination:
                    yield combination
            else:
                for c in self.num_map[digits[0]]:
                    new_combination = combination+c
                    yield from translate(new_combination, digits[1:])

        return list(translate("", digits))


s = Solution()

digits = "23"
print(digits)
print(s.letterCombinations(digits))

# 68
from typing import List

class Solution:
    space = " "

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rows = []
        row_words = []
        lwords = 0
        lline = 0
        for w in words:
            l = len(w)
            if lline + l > maxWidth:
                if len(row_words) == 1:
                    rows.append(row_words[0] + self.space*(maxWidth - lwords))
                else:
                    spaces, extra = divmod(maxWidth - lwords, len(row_words) - 1)
                    # print(row_words, spaces, extra, len(row_words), maxWidth, len(row_words) - 1)
                    row = ""
                    while row_words:
                        row += row_words.pop(0)
                        if row_words:
                            row += self.space*spaces
                            row += self.space if extra > 0 else ""
                            extra -= 1
                    rows.append(row)

                row_words = []
                lwords = 0
                lline = 0

            row_words.append(w)
            lwords += l
            lline += l + 1

        if row_words:
            rows.append(self.space.join(row_words) + self.space*(maxWidth - lline + 1))

        return rows


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(words)
print(maxWidth)
print("\n".join(Solution().fullJustify(words, maxWidth)))

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(words)
print(maxWidth)
print("\n".join(Solution().fullJustify(words, maxWidth)))

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(words)
print(maxWidth)
print("\n".join(Solution().fullJustify(words, maxWidth)))

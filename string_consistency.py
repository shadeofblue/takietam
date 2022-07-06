from typing import List
from functools import partial


def check_consistency(allowed: str, word: str):
    return set(allowed) >= set(word)


def count_consistent(allowed: str, words: List[str]):
    return len(list(filter(partial(check_consistency, allowed), words)))


print(count_consistent("ab", ["ad","bd","aaab","baa","badab"]))
print(count_consistent("abc", ["a","b","c","ab","ac","bc","abc"]))
print(count_consistent("acd", ["cc","acd","b","ba","bac","bad","ac","d"]))


from typing import Dict, List
from pathlib import Path

input_cypher = input("input cypher: ")

WORDFILE = Path("/usr/share/dict/polish")

def word_dict(s: str):
    s_dict = {}
    for c in s:
        s_dict.setdefault(c, 0)
        s_dict[c] += 1
    return s_dict


def is_anagram(src: str, tgt: str):
    if len(src) != len(tgt):
        return []

    return word_dict(src) == word_dict(tgt)

def combine(cypher_words: List[str], cypher_map: Dict[str, List[str]]):
    counters = [0 for _ in range(len(cypher_words))]

    done = False
    while not done:
        # print(f"{counters=}, {cypher_words=}, {cypher_map=}")
        combination = []
        for i in range(len(cypher_words)):
            combination.append(cypher_map[cypher_words[i]][counters[i]])
        yield combination

        counters[0] += 1
        for c in range(len(counters)):
            if counters[c] >= len(cypher_map[cypher_words[c]]):
                if c < len(counters) - 1:
                    for cc in range(c + 1):
                        counters[cc] = 0
                    counters[c + 1] += 1
                else:
                    done = True


def find_solution(cypher: str, wordfile: Path) -> Dict[str, List[str]]:
    cypher_words = [w.lower() for w in cypher.split(" ")]
    cypher_map: Dict[str, List[str]] = {w: [] for w in cypher_words}

    with wordfile.open("r") as f:
        while True:
            w = f.readline().strip().lower()
            if not w:
                break
            for cw in cypher_map.keys():
                if is_anagram(cw, w) and w not in cypher_map[cw]:
                    cypher_map[cw].append(w)

    return cypher_map

possible_solutions = find_solution(input_cypher, WORDFILE)
print(possible_solutions)
for s in combine([w.lower() for w in input_cypher.split(" ")], possible_solutions):
    print(" ".join(s))

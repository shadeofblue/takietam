# 433
from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Gene:
    seq: str
    mutations: List["Gene"] = field(default_factory=list)
    visited = False

    def __repr__(self):
        return f"Gene<{self.seq} mutations={[g.seq for g in self.mutations]}>"


class Solution:
    def mutation_possible(self, g1: str, g2: str):
        assert len(g1) == len(g2)
        return len(list(filter(lambda pair: pair[0] != pair[1], zip(g1, g2)))) == 1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        genes: Dict[str, Gene] = {startGene: Gene(startGene)}
        for seq in bank:
            genes[seq] = Gene(seq)

        for src_gene in genes.values():
            for tgt_gene in genes.values():
                if self.mutation_possible(src_gene.seq, tgt_gene.seq):
                    src_gene.mutations.append(tgt_gene)

        # print(genes)

        candidates = [genes[startGene]]
        mutations = 0
        while candidates and not genes[endGene] in candidates:
            candidates_next: List[Gene] = []
            mutations += 1
            for c in candidates:
                if c.visited:
                    continue
                candidates_next.extend(c.mutations)
                c.visited = True
            candidates = candidates_next

        return mutations if candidates else -1


s = Solution()


startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
print(f"{startGene=}, {endGene=}, {bank=}")
print(s.minMutation(startGene, endGene, bank))

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(f"{startGene=}, {endGene=}, {bank=}")
print(s.minMutation(startGene, endGene, bank))


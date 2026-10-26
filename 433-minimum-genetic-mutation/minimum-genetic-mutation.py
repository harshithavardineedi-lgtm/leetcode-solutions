from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}
        genes = "ACGT"

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for char in genes:
                    if char == gene[i]:
                        continue

                    new_gene = gene[:i] + char + gene[i + 1:]

                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))

        return -1    
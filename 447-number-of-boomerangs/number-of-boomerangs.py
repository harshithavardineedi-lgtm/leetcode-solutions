from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0

        for x1, y1 in points:
            count = defaultdict(int)

            for x2, y2 in points:
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                count[d] += 1

            for c in count.values():
                result += c * (c - 1)

        return result    
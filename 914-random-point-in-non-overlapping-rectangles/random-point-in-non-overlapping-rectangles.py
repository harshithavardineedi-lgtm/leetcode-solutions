import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0

        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)

    def pick(self) -> List[int]:
        k = random.randint(1, self.prefix[-1])
        i = bisect.bisect_left(self.prefix, k)

        x1, y1, x2, y2 = self.rects[i]
        width = x2 - x1 + 1

        k -= self.prefix[i - 1] if i > 0 else 0

        return [x1 + (k - 1) % width,
                y1 + (k - 1) // width]
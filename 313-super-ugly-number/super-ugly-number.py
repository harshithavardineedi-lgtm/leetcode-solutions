from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]

        heap = []
        for p in primes:
            heapq.heappush(heap, (p, p, 0))

        while len(ugly) < n:
            value, prime, index = heapq.heappop(heap)

            if value != ugly[-1]:
                ugly.append(value)

            next_index = index + 1
            next_value = prime * ugly[next_index]
            heapq.heappush(heap, (next_value, prime, next_index))

        return ugly[-1]    
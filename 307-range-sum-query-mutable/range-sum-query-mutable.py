
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        for i, num in enumerate(nums, 1):
            self._add(i, num)

    def _add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def _prefix_sum(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)

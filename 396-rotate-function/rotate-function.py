from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)
        current = sum(i * num for i, num in enumerate(nums))
        maximum = current

        for i in range(n - 1, 0, -1):
            current = current + total - n * nums[i]
            maximum = max(maximum, current)

        return maximum    
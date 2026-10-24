from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums, count):
            drop = len(nums) - count
            stack = []

            for digit in nums:
                while drop and stack and stack[-1] < digit:
                    stack.pop()
                    drop -= 1
                stack.append(digit)

            return stack[:count]

        def merge(a, b):
            result = []
            i = j = 0

            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1

            return result

        best = []

        for take1 in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            take2 = k - take1
            a = pick_max(nums1, take1)
            b = pick_max(nums2, take2)
            candidate = merge(a, b)

            if candidate > best:
                best = candidate

        return best    
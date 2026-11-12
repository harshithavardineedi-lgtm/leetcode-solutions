class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        seen = {0: -1}
        result = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in seen:
                result = max(result, i - seen[count])
            else:
                seen[count] = i

        return result    
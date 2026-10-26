from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = Counter(s)

        for char in count:
            if count[char] < k:
                return max(
                    self.longestSubstring(part, k)
                    for part in s.split(char)
                )

        return len(s)    
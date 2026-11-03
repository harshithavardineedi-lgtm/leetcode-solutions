from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        k = len(p)

        if k > len(s):
            return result

        p_count = Counter(p)
        window = Counter(s[:k])

        if window == p_count:
            result.append(0)

        for i in range(k, len(s)):
            window[s[i]] += 1
            window[s[i - k]] -= 1

            if window[s[i - k]] == 0:
                del window[s[i - k]]

            if window == p_count:
                result.append(i - k + 1)

        return result    
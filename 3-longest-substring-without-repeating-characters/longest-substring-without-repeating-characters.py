class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        max_len = 0
        char_set = set()

        while i < len(s):
            if s[i] not in char_set:
                char_set.add(s[i])
                i += 1
                max_len = max(max_len, len(char_set))
            else:
                char_set.remove(s[j])
                j += 1

        return max_len
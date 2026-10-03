class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_index = 0
        p_index = 0
        star = -1
        match = 0

        while s_index < len(s):
            if p_index < len(p) and (p[p_index] == "?" or p[p_index] == s[s_index]):
                s_index += 1
                p_index += 1

            elif p_index < len(p) and p[p_index] == "*":
                star = p_index
                match = s_index
                p_index += 1

            elif star != -1:
                p_index = star + 1
                match += 1
                s_index = match

            else:
                return False

        while p_index < len(p) and p[p_index] == "*":
            p_index += 1

        return p_index == len(p)    
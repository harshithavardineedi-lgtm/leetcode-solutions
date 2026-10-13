class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_e = False
        digit_after_e = True

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
                if seen_e:
                    digit_after_e = True

            elif ch in "+-":
                if i > 0 and s[i - 1] not in "eE":
                    return False

            elif ch == ".":
                if seen_dot or seen_e:
                    return False
                seen_dot = True

            elif ch in "eE":
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                digit_after_e = False

            else:
                return False

        return seen_digit and digit_after_e

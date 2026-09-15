class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        sign = 1
        index = 0

        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        num = 0

        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        num *= sign

        num = max(-2**31, min(num, 2**31 - 1))

        return num    
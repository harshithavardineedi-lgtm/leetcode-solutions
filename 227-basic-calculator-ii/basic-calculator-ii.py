class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        sign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-number)
                elif sign == '*':
                    stack.append(stack.pop() * number)
                elif sign == '/':
                    top = stack.pop()
                    stack.append(int(top / number))

                sign = char
                number = 0

        return sum(stack)
    
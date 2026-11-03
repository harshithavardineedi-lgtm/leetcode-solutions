class Solution:
    def rand10(self):
        while True:
            a = rand7()
            b = rand7()

            num = (a - 1) * 7 + b

            if num <= 40:
                return (num - 1) % 10 + 1
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            value = divisor
            multiple = 1

            while dividend >= value + value:
                value += value
                multiple += multiple

            dividend -= value
            result += multiple

        if negative:
            result = -result

        return result    
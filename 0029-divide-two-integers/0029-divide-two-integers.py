class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        a, b = abs(dividend), abs(divisor)

        result = 0
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple

        if negative:
            result = -result

        return max(INT_MIN, min(INT_MAX, result))
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        x = int(str(x_abs)[::-1])
        result = x * sign
        if -2 ** 31 <= result <= (2 ** 31) - 1:
            return result
        return 0
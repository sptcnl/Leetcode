class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = int(str(x)[::-1].replace('-', ''))
        result = x * sign
        if -2 ** 31 <= result <= (2 ** 31) - 1:
            return result
        return 0
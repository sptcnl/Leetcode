class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        x = str(x)
        if x[0] == "-" or sign == "+":
            sign = -1 if x[0] == "-" else 1
            x = x[1:]
        x = x[::-1]
        x = int(x) * sign
        if (-2 ** 31) <= x <= ((2 ** 31) - 1):
            return x
        else:
            return 0
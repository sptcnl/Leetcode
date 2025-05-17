import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        if s and (s[0] == "-" or s[0] == "+"):
            sign = -1 if s[0] == "-" else 1
            s = s[1:]

        result = 0
        for w in s:
            if w.isdigit():
                result = result * 10 + int(w)
            else:
                break

        result *= sign

        min_int = -2 ** 31
        max_int = (2 ** 31) - 1

        if result < min_int:
            return min_int
        elif result > max_int:
            return max_int
        else:
            return result
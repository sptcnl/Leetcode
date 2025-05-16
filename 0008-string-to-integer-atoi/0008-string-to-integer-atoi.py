import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        if s[0] in ('+', '-'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        num_str = []
        for c in s:
            if not c.isdigit():
                break
            num_str.append(c)
        
        if not num_str:
            return 0
        
        num = int(''.join(num_str)) * sign
        return max(min(num, 2**31-1), -2**31)
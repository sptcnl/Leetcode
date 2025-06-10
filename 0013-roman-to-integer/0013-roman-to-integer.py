class Solution:
    def to_int(self, s, s_idx):
        if s[s_idx] == "I":
            if not ((s_idx + 1) == len(s)):
                if s[s_idx + 1] == "V":
                    return (s_idx + 1), 4
                elif s[s_idx + 1] == "X":
                    return (s_idx + 1), 9
            return s_idx, 1
        elif s[s_idx] == "V":
            return s_idx, 5
        elif s[s_idx] == "X":
            if not ((s_idx + 1) == len(s)):
                if s[s_idx + 1] == "L":
                    return (s_idx + 1), 40
                elif s[s_idx + 1] == "C":
                    return (s_idx + 1), 90
            return s_idx, 10
        elif s[s_idx] == "L":
            return s_idx, 50
        elif s[s_idx] == "C":
            if not ((s_idx + 1) == len(s)):
                if s[s_idx + 1] == "D":
                    return (s_idx + 1), 400
                elif s[s_idx + 1] == "M":
                    return (s_idx + 1), 900
            return s_idx, 100
        elif s[s_idx] == "D":
            return s_idx, 500
        elif s[s_idx] == "M":
            return s_idx, 1000

    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            j, num = self.to_int(s, i)
            i = j
            result += num
            i += 1
        return result
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        for i in t:
            s_dict[i] -= 1
        s_dict_value = s_dict.values()
        print(s_dict_value)
        for i in s_dict_value:
            if i != 0:
                return False
        return True
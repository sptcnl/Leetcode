import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = s.lower()
        strs = re.sub('[^a-z0-9]', '', strs)
        if strs == strs[::-1]:
            return True
        return False
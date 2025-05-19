class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result_str = ""
        for i, s in enumerate(zip(*strs)):
            if len(set(s)) != 1:
                return result_str
            else:
                result_str += strs[0][i]
            
        return result_str
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        start = 0
        max_len = 0
        for end, ch in enumerate(s):
            if ch in index_map:
                start = max(start, index_map[ch] + 1)
            index_map[ch] = end
            max_len = max(max_len, end - start + 1)
        return max_len
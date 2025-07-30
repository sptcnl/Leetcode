from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        max_key = max(d, key=d.get)
        return max_key
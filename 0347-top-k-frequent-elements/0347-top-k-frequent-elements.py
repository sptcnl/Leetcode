from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        result = [k for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]
        return result
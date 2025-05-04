from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = defaultdict(int)
        result = []
        
        for num in nums1:
            freq[num] += 1
        
        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1
                
        return result
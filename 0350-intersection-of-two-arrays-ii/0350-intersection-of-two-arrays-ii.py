from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        num1_dict = defaultdict(int)
        for num in nums1:
            num1_dict[num] += 1

        for num in nums2:
            if num1_dict[num] > 0:
                num1_dict[num] -= 1
                result.append(num)
        
        return result
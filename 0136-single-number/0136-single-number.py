class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[0]
        for i in range(1,len(nums)):
            n ^= nums[i]
        return n
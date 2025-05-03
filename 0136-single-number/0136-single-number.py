class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = 1
        for _ in range(0, len(nums)):
            if len(nums) == 1:
                return nums[0]
            if i == len(nums)-1:
                return nums[i]
            if nums[i] == nums[j]:
                i = j+1
                j = i+1
            else:
                return nums[i]
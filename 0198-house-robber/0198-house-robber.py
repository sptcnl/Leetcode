class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        prev = nums[0]
        curr = max(nums[0], nums[1])
        for num in nums[2:]:
            prev, curr = curr, max(curr, prev + num)
        return curr
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        prev = nums[0]
        cur_num = max(nums[0], nums[1])

        for num in nums[2:]:
            prev, cur_num = cur_num, max(cur_num, prev + num)

        return cur_num
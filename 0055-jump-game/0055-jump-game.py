class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False  # 현재 위치까지 못 도달한다면 실패
            max_reach = max(max_reach, i + nums[i])
        return True
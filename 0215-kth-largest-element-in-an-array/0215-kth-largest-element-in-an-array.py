class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        idx = -k
        nums.sort()
        return nums[idx]
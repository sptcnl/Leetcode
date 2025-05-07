class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                i_plus_j = nums[i] + nums[j]
                if i_plus_j == target:
                    result.append(i)
                    result.append(j)
        return result
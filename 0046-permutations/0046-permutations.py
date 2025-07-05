class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        result = []
        def backtrack(path, used):
            if len(path) == len_nums:
                result.append(path[:])
                return
            for i in range(len_nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        backtrack([], [False]*len_nums)
        return result
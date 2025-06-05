import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        array = self.nums[:]
        n = len(array)
        for i in range(n):
            j = random.randint(i, n - 1)  # i 이상 n-1 이하 중 무작위 인덱스
            array[i], array[j] = array[j], array[i]  # 두 원소를 swap
        return array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
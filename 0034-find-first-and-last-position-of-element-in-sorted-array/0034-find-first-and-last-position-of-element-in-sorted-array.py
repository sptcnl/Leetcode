class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        ans = mid
                    right = mid - 1
            return ans

        def find_right():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        ans = mid
                    left = mid + 1
            return ans

        return [find_left(), find_right()]
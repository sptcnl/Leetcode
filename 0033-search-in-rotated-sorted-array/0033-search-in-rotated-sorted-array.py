class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 1. 정답을 찾은 경우
            if nums[mid] == target:
                return mid

            # 2. 왼쪽 구간이 정렬되어 있는 경우
            if nums[left] <= nums[mid]:
                # target이 정렬된 왼쪽 구간에 있는 경우
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:  # 아니면 오른쪽 구간으로
                    left = mid + 1

            # 3. 오른쪽 구간이 정렬되어 있는 경우
            else:
                # target이 정렬된 오른쪽 구간에 있는 경우
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:  # 아니면 왼쪽 구간으로
                    right = mid - 1

        # 못 찾은 경우
        return -1
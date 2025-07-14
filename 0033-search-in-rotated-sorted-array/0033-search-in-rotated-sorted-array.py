class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 탐색 범위의 시작(left)과 끝(right) 인덱스 설정

        while left <= right:    # 탐색 범위가 유효할 때까지 반복
            mid = (left + right) // 2   # 중간 인덱스 계산

            # 1. 정답을 찾은 경우
            if nums[mid] == target: # 중간 값이 target과 같으면
                return mid  # 해당 인덱스 반환

            # 2. 왼쪽 구간이 정렬되어 있는 경우
            if nums[left] <= nums[mid]: # 왼쪽 구간이 정렬되어 있으면
                # target이 정렬된 왼쪽 구간에 있는 경우
                if nums[left] <= target < nums[mid]:    # target이 왼쪽 구간에 있으면
                    right = mid - 1 # 탐색 범위를 왼쪽으로 좁힘
                else:  # 아니면 오른쪽 구간으로
                    left = mid + 1  # 탐색 범위를 오른쪽으로 좁힘

            # 3. 오른쪽 구간이 정렬되어 있는 경우
            else:
                # target이 정렬된 오른쪽 구간에 있는 경우
                if nums[mid] < target <= nums[right]:   # target이 오른쪽 구간에 있으면
                    left = mid + 1  # 탐색 범위를 오른쪽으로 좁힘
                else:  # 아니면 왼쪽 구간으로
                    right = mid - 1 # 탐색 범위를 왼쪽으로 좁힘

        # 못 찾은 경우
        return -1
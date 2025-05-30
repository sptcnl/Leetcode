class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # nums1의 마지막 유효 원소 인덱스
        j = n - 1  # nums2의 마지막 원소 인덱스
        k = m + n - 1  # 병합된 배열의 마지막 위치
        
        # 역방향으로 큰 값부터 채우기
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # nums2에 남은 원소가 있는 경우 처리
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
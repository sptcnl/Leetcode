class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for x in range(len(nums) - 2):  # 첫 번째 원소 고정
            if x > 0 and nums[x] == nums[x-1]:  # 중복 제거
                continue
            
            left, right = x + 1, len(nums) - 1  # 투포인터 설정
            
            while left < right:
                total = nums[x] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[x], nums[left], nums[right]])
                    # 중복 원소 건너뛰기
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
        return result
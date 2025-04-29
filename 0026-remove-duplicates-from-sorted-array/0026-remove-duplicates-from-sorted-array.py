class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0 
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]: # 중복된 수가 아니라면
                i+=1  # i를 옮기고
                nums[i]=nums[j] # nums의 i번째 수를 nums의 j번째 수로 바꾸기
        
        return i+1
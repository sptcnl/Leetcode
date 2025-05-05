class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        num = ""
        for digit in digits:
            num = num + str(digit)
        
        num_plus = str(int(num) + 1)

        for i in num_plus:
            result.append(int(i))

        return result
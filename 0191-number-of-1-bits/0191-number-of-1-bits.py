class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([i for i in str(bin(n)) if i == "1"])
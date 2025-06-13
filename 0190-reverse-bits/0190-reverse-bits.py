class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:].zfill(32)
        result = 0
        for i in range(len(n)):
            if n[i] == "1":
                result += (2 ** i)
        return result
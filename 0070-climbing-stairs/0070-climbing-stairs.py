import math

class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        fib_n = (phi**(n+1) - psi**(n+1)) / sqrt5
        return int(round(fib_n))
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        n_list = [True] * n
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if n_list[i] == True:
                for j in range(i + i, n, i):
                    n_list[j] = False
        return len([i for i in range(2, n) if n_list[i] == True])
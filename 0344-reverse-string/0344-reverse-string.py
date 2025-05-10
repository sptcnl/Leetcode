class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        if len_s % 2 == 0:
            rotate_range = len_s // 2
        else: rotate_range = (len_s - 1) // 2

        j = -1
        for i in range(rotate_range):
            bf_i = s[i]
            s[i] = s[j]
            s[j] = bf_i
            j -= 1
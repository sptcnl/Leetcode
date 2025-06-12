class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = format(x, 'b')
        y_bin = format(y, 'b')
        max_len = max(len(x_bin), len(y_bin))
        x_bin = x_bin.zfill(max_len)
        y_bin = y_bin.zfill(max_len)
        count = 0
        for a, b in zip(x_bin, y_bin):
            if a != b:
                count += 1
        return count

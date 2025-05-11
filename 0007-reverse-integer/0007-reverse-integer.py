class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs_str = str(abs(x))
        reversed_str = x_abs_str[::-1]
        reversed_int = sign * int(reversed_str)
        # 32비트 정수 범위 체크
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int
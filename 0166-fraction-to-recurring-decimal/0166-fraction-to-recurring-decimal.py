class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        result = []
        # 부호 처리
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
        n, d = abs(numerator), abs(denominator)
        result.append(str(n // d))
        n %= d
        if n == 0:
            return ''.join(result)
        result.append('.')
        pos_map = {}
        while n:
            if n in pos_map:
                result.insert(pos_map[n], '(')
                result.append(')')
                break
            pos_map[n] = len(result)
            n *= 10
            result.append(str(n // d))
            n %= d
        return ''.join(result)
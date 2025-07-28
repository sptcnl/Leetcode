class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 1. 분자가 0이면 그냥 0 반환
        if numerator == 0:
            return "0"

        result = []

        # 2. 부호 처리 (음수 판별: 두 수 중 하나만 음수)
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
        
        # 3. 절댓값 변환
        n, d = abs(numerator), abs(denominator)

        # 4. 정수 부분 먼저 결과에 추가
        result.append(str(n // d))
        n %= d    # 정수 부분 이후의 나머지

        # 5. 소수 부분 없으면 바로 리턴 (정수 나누어떨어짐)
        if n == 0:
            return ''.join(result)

        # 6. 소수점 붙임
        result.append('.')

        # 7. 순환(반복) 소수 구간 추적용 딕셔너리
        pos_map = {}

        # 8. 나머지가 0이 될 때까지(=끝까지) 혹은, 순환이 검출될 때까지 반복
        while n:
            if n in pos_map:
                # 순환이 발생, 반복 시작 위치에 '(' 삽입하고, 마지막에 ')' 추가
                result.insert(pos_map[n], '(')
                result.append(')')
                break
            # 현재 나머지의 자리 인덱스를 기록
            pos_map[n] = len(result)
            n *= 10
            result.append(str(n // d))
            n %= d

        return ''.join(result)
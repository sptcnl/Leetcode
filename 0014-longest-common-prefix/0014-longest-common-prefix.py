class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # zip(*strs)로 각 인덱스별 문자들을 튜플로 묶음
        for i, chars in enumerate(zip(*strs)):
            # set(chars)가 1개(모두 같음)인지 확인
            if len(set(chars)) != 1:
                return strs[0][:i]  # 첫 번째 문자열의 0~i까지가 공통 접두사
        # 모두 같으면 가장 짧은 문자열 전체가 접두사
        return min(strs, key=len)
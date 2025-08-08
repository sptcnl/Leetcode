class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(idx, path):
            # idx: path 인덱스, path: 현재까지 만들어진 문자열
            print(f"Index: {idx}, Path: '{path}'")
            if idx == len(digits):
                print(f"완성된 조합: '{path}'\n")
                result.append(path)
                return

            possible_chars = phone_map[digits[idx]]
            print(f"현재 숫자 '{digits[idx]}'에 매핑된 문자들: {possible_chars}")
            for c in possible_chars:
                print(f"문자 '{c}'를 추가하여 재귀 호출")
                backtrack(idx + 1, path + c)
        
        backtrack(0, "")
        return result
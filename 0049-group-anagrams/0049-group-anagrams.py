from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)
        result = []

        for string in strs:
            sorted_str = tuple(sorted(string))
            print(string, sorted_str)
            freq_dict[sorted_str].append(string)

        # 결과 추출
        result = list(freq_dict.values())
        return result
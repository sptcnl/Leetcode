class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        output = []

        words2_dict = {}
        words1_dict = {}

        for i in words2:
            set_i = list(set(list(i)))
            for j in set_i:
                if j not in words2_dict.keys() or words2_dict[j] < i.count(j):
                    words2_dict[j] = i.count(j)
        for i in words1:
            words1_dict = Counter(i)
            for j in words2_dict.keys():
                if j not in words1_dict.keys() or words1_dict[j] < words2_dict[j]:
                    break
            else:
                output.append(i)

        return output